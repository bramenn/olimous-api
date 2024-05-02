from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..category.consultas import get_category_id_db
from .modelo import Tournament, TournamentIn, TournamentOut


def get_all_tournaments_db() -> TournamentOut:
    tournaments = db.session.query(Tournament)

    if not tournaments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournaments no encontradas",
        )

    return [parse_tournament(tournament) for tournament in tournaments]


def get_tournament_id_db(id: str) -> TournamentOut:
    tournament = db.session.query(Tournament).where(Tournament.id == id).first()

    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament no encontrada",
        )

    return parse_tournament(tournament)


def get_tournament_manager_id_db(id: str) -> TournamentOut:
    tournament = db.session.query(Tournament).where(Tournament.id == id).first()

    if not tournament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament no encontrada",
        )

    return parse_tournament(tournament)


def get_created_free_tournament_db(tournament: TournamentIn) -> int:
    category = get_category_id_db(tournament.category_id)

    if not category.is_free:
        return 0

    return (
        db.session.query(Tournament)
        .where(
            Tournament.manager_id == tournament.manager_id
            and Tournament.category_id == category.id
        )
        .count()
    )


def create_tournament_db(
    new_tournament: TournamentIn,
) -> TournamentOut:

    created_tournaments = get_created_free_tournament_db(new_tournament)

    if created_tournaments >= 2:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya has creado el maximo de torneos gratuitos",
        )

    print(new_tournament.date)

    tournament = Tournament(
        manager_id=new_tournament.manager_id,
        category_id=new_tournament.category_id,
        game_id=new_tournament.game_id,
        date=new_tournament.date,
        cost_view=new_tournament.cost_view,
        cost_competitor=new_tournament.cost_competitor,
        name=new_tournament.name,
    )

    try:
        db.session.add(tournament)
        db.session.commit()
        return parse_tournament(tournament)
    except Exception as e:
        print("No se ha creado la tournament: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la tournament",
        )


def parse_tournament(tournament: Tournament) -> TournamentOut:
    return TournamentOut(
        id=tournament.id,
        manager_id=tournament.manager_id,
        category_id=tournament.category_id,
        game_id=tournament.game_id,
        date=tournament.date.__str__(),
        cost_view=tournament.cost_view,
        cost_competitor=tournament.cost_competitor,
        name=tournament.name,
    )
