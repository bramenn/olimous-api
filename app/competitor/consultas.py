from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Competitor, CompetitorIn, CompetitorOut


def get_all_competitors_db() -> CompetitorOut:
    competitors = db.session.query(Competitor)

    if not competitors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Competitors no encontradas",
        )

    return [parse_competitor(competitor) for competitor in competitors]


def get_competitor_id_db(id: str) -> CompetitorOut:
    competitor = db.session.query(Competitor).where(Competitor.id == id).first()

    if not competitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Competitor no encontrada",
        )

    return parse_competitor(competitor)


def create_competitor_db(
    new_competitor: CompetitorIn,
) -> CompetitorOut:
    competitor = Competitor(
        name=new_competitor.name,
        email=new_competitor.email,
        alias=new_competitor.alias,
        phone=new_competitor.phone,
    )

    try:
        db.session.add(competitor)
        db.session.commit()
        return parse_competitor(competitor)
    except Exception as e:
        print("No se ha creado la competitor: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la competitor",
        )


def parse_competitor(competitor: Competitor) -> CompetitorOut:
    return CompetitorOut(
        id=competitor.id,
        name=competitor.name,
        email=competitor.email,
        alias=competitor.alias,
        phone=competitor.phone,
    )
