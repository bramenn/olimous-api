from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Game, GameIn, GameOut


def get_all_games_db() -> GameOut:
    games = db.session.query(Game)

    if not games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Games no encontradas",
        )

    return [parse_game(game) for game in games]


def get_game_id_db(id: str) -> GameOut:
    game = db.session.query(Game).where(Game.id == id).first()

    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game no encontrada",
        )

    return parse_game(game)


def create_game_db(
    new_game: GameIn,
) -> GameOut:
    game = Game(name=new_game.name)

    try:
        db.session.add(game)
        db.session.commit()
        return parse_game(game)
    except Exception as e:
        print("No se ha creado la game: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la game",
        )


def parse_game(game: Game) -> GameOut:
    return GameOut(id=game.id, name=game.name)
