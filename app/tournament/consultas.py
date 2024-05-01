from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
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


def create_tournament_db(
    new_tournament: TournamentIn,
) -> TournamentOut:
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
