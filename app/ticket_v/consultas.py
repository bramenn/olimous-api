from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import TicketViewer, TicketViewerIn, TicketViewerOut


def get_all_ticket_viewers_db() -> TicketViewerOut:
    ticket_viewers = db.session.query(TicketViewer)

    if not ticket_viewers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketViewers no encontradas",
        )

    return [parse_ticket_viewer(ticket_viewer) for ticket_viewer in ticket_viewers]


def get_ticket_viewer_id_db(id: str) -> TicketViewerOut:
    ticket_viewer = db.session.query(TicketViewer).where(TicketViewer.id == id).first()

    if not ticket_viewer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketViewer no encontrada",
        )

    return parse_ticket_viewer(ticket_viewer)


def create_ticket_viewer_db(
    new_ticket_viewer: TicketViewerIn,
) -> TicketViewerOut:
    ticket_viewer = TicketViewer(
        tournament_id=new_ticket_viewer.tournament_id,
        viewer_id=new_ticket_viewer.viewer_id,
        qr_code=new_ticket_viewer.qr_code,
        is_active=new_ticket_viewer.is_active,
        was_use=new_ticket_viewer.was_use,
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


def parse_ticket_viewer(ticket_viewer: TicketViewer) -> TicketViewerOut:
    return TicketViewerOut(
        id=ticket_viewer.id,
        tournament_id=ticket_viewer.tournament_id,
        viewer_id=ticket_viewer.viewer_id,
        qr_code=ticket_viewer.qr_code,
        is_active=ticket_viewer.is_active,
        was_use=ticket_viewer.was_use,
    )
