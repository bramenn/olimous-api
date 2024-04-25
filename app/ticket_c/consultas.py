from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import TicketCompetitor, TicketCompetitorIn, TicketCompetitorOut


def get_all_ticket_competitors_db() -> TicketCompetitorOut:
    ticket_competitors = db.session.query(TicketCompetitor)

    if not ticket_competitors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketCompetitors no encontradas",
        )

    return [parse_ticket_competitor(ticket_competitor) for ticket_competitor in ticket_competitors]


def get_ticket_competitor_id_db(id: str) -> TicketCompetitorOut:
    ticket_competitor = db.session.query(TicketCompetitor).where(TicketCompetitor.id == id).first()

    if not ticket_competitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TicketCompetitor no encontrada",
        )

    return parse_ticket_competitor(ticket_competitor)


def create_ticket_competitor_db(
    new_ticket_competitor: TicketCompetitorIn,
) -> TicketCompetitorOut:
    ticket_competitor = TicketCompetitor(
        tournament_id=new_ticket_competitor.tournament_id,
        competitor_id=new_ticket_competitor.competitor_id,
        qr_code=new_ticket_competitor.qr_code,
        is_active=new_ticket_competitor.is_active,
        was_use=new_ticket_competitor.was_use,
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


def parse_ticket_competitor(ticket_competitor: TicketCompetitor) -> TicketCompetitorOut:
    return TicketCompetitorOut(
        id=ticket_competitor.id,
        tournament_id=ticket_competitor.tournament_id,
        competitor_id=ticket_competitor.competitor_id,
        qr_code=ticket_competitor.qr_code,
        is_active=ticket_competitor.is_active,
        was_use=ticket_competitor.was_use,
    )
