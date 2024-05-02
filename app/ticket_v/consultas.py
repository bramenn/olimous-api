from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..category.consultas import get_category_id_db
from ..tournament.consultas import get_tournament_id_db
from ..utils.generate_qr import qr_str
from .modelo import TicketViewer, TicketViewerIn, TicketViewerOut


def get_all_ticket_viewers_db() -> TicketViewerOut:
    ticket_viewers = db.session.query(TicketViewer)

    if not ticket_viewers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketViewers no encontradas",
        )

    return [parse_ticket_viewer(ticket_viewer) for ticket_viewer in ticket_viewers]


def get_tickets_viewer_by_tournament_id_db(tournament_id: int) -> int:
    tickets = (
        db.session.query(TicketViewer).where(TicketViewer.tournament_id == tournament_id).count()
    )
    return tickets


def get_ticket_viewer_id_db(id: str) -> TicketViewerOut:
    ticket_viewer = db.session.query(TicketViewer).where(TicketViewer.id == id).first()

    if not ticket_viewer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketViewer no encontrada",
        )

    return parse_ticket_viewer(ticket_viewer)


def get_ticket_viewer_qr_code_db(qr_code: str) -> TicketViewerOut:
    print(qr_code)
    ticket_viewer = db.session.query(TicketViewer).where(TicketViewer.qr_code == qr_code).first()

    if not ticket_viewer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketViewer no encontrada",
        )

    ticket_viewer.was_use = True
    db.session.commit()

    return parse_ticket_viewer(ticket_viewer)


def create_ticket_viewer_db(
    new_ticket_viewer: TicketViewerIn,
) -> TicketViewerOut:
    tickets_sold = get_tickets_viewer_by_tournament_id_db(new_ticket_viewer.tournament_id)

    tournament = get_tournament_id_db(new_ticket_viewer.tournament_id)
    category = get_category_id_db(tournament.category_id)

    if tickets_sold >= category.limit_participants:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se pueden vender mas ticket para este torneo ya que has sobrepasado la cantidad maxima",
        )

    ticket_viewer = TicketViewer(
        tournament_id=new_ticket_viewer.tournament_id,
        viewer_id=new_ticket_viewer.viewer_id,
        qr_code=qr_str(new_ticket_viewer.tournament_id, new_ticket_viewer.viewer_id),
    )

    try:
        db.session.add(ticket_viewer)
        db.session.commit()
        return parse_ticket_viewer(ticket_viewer)
    except Exception as e:
        print("No se ha creado la ticket_viewer: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la ticket_viewer",
        )


def generate_cost_commission_and_total_price(ticket: TicketViewer) -> tuple:
    tournament = get_tournament_id_db(ticket.tournament_id)
    category = get_category_id_db(tournament.category_id)

    cost_commission = tournament.cost_competitor * category.commission
    total_price = tournament.cost_competitor + cost_commission

    return cost_commission, total_price


def parse_ticket_viewer(ticket_viewer: TicketViewer) -> TicketViewerOut:
    cost_commission, total_price = generate_cost_commission_and_total_price(ticket_viewer)
    return TicketViewerOut(
        id=ticket_viewer.id,
        tournament_id=ticket_viewer.tournament_id,
        viewer_id=ticket_viewer.viewer_id,
        qr_code=ticket_viewer.qr_code,
        is_active=ticket_viewer.is_active,
        was_use=ticket_viewer.was_use,
        total_price=total_price,
        commission=cost_commission,
    )
