from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_game_db, get_all_games_db, get_game_id_db
from .modelo import GameIn, GameOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[GameOut],
    status_code=200,
    summary="Obtenga todas las categorias",
    description="Multiples categorias seran entregados en una lista de json, separados por comas ",
    operation_id="getGames",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_games():
    games = get_all_games_db()
    return games


@router.get(
    "/{id}",
    response_model=GameOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getGame",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_game_id(id: str):
    game = get_game_id_db(id)
    return game


@router.post(
    "/",
    response_model=GameOut,
    status_code=200,
    summary="Cree una categoria",
    description="Cree una categoria enviando sus datos en un JSON",
    operation_id="createGame",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_game(nuevo_game: GameIn):
    game = create_game_db(nuevo_game)
    return game
