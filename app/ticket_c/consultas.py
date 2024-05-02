from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..category.consultas import get_category_id_db
from ..tournament.consultas import get_tournament_id_db
from ..utils.generate_qr import qr_str
from .modelo import TicketCompetitor, TicketCompetitorIn, TicketCompetitorOut


def get_all_ticket_competitors_db() -> TicketCompetitorOut:
    ticket_competitors = db.session.query(TicketCompetitor)

    if not ticket_competitors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketCompetitors no encontradas",
        )

    return [parse_ticket_competitor(ticket_competitor) for ticket_competitor in ticket_competitors]


def get_tickets_competitors_by_tournament_id_db(tournament_id: int) -> int:
    tickets = (
        db.session.query(TicketCompetitor)
        .where(TicketCompetitor.tournament_id == tournament_id)
        .count()
    )
    return tickets


def get_ticket_competitor_id_db(id: str) -> TicketCompetitorOut:
    ticket_competitor = db.session.query(TicketCompetitor).where(TicketCompetitor.id == id).first()

    if not ticket_competitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketCompetitor no encontrada",
        )

    return parse_ticket_competitor(ticket_competitor)


def get_ticket_competitor_qr_code_db(qr_code: str) -> TicketCompetitorOut:
    print(qr_code)
    ticket_competitor = (
        db.session.query(TicketCompetitor).where(TicketCompetitor.qr_code == qr_code).first()
    )

    if not ticket_competitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketCompetitor no encontrada",
        )

    ticket_competitor.was_use = True
    db.session.commit()

    return parse_ticket_competitor(ticket_competitor)


def create_ticket_competitor_db(
    new_ticket_competitor: TicketCompetitorIn,
) -> TicketCompetitorOut:
    tickets_sold = get_tickets_competitors_by_tournament_id_db(new_ticket_competitor.tournament_id)

    tournament = get_tournament_id_db(new_ticket_competitor.tournament_id)
    category = get_category_id_db(tournament.category_id)

    if tickets_sold >= category.limit_participants:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se pueden vender mas ticket para este torneo ya que has sobrepasado la cantidad maxima",
        )

    ticket_competitor = TicketCompetitor(
        tournament_id=new_ticket_competitor.tournament_id,
        competitor_id=new_ticket_competitor.competitor_id,
        qr_code=qr_str(new_ticket_competitor.tournament_id, new_ticket_competitor.competitor_id),
    )
    try:
        db.session.add(ticket_competitor)
        db.session.commit()
        return parse_ticket_competitor(ticket_competitor)
    except Exception as e:
        print("No se ha creado la ticket_competitor: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la ticket_competitor",
        )


def generate_cost_commission_and_total_price(ticket: TicketCompetitor) -> tuple:
    tournament = get_tournament_id_db(ticket.tournament_id)
    category = get_category_id_db(tournament.category_id)

    cost_commission = tournament.cost_competitor * category.commission
    total_price = tournament.cost_competitor + cost_commission

    return cost_commission, total_price


def parse_ticket_competitor(ticket_competitor: TicketCompetitor) -> TicketCompetitorOut:
    cost_commission, total_price = generate_cost_commission_and_total_price(ticket_competitor)
    return TicketCompetitorOut(
        id=ticket_competitor.id,
        tournament_id=ticket_competitor.tournament_id,
        competitor_id=ticket_competitor.competitor_id,
        qr_code=ticket_competitor.qr_code,
        is_active=ticket_competitor.is_active,
        was_use=ticket_competitor.was_use,
        total_price=total_price,
        commission=cost_commission,
    )
