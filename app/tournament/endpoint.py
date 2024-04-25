from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_tournament_db, get_all_tournaments_db, get_tournament_id_db
from .modelo import TournamentIn, TournamentOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[TournamentOut],
    status_code=200,
    summary="Obtenga todas las categorias",
    description="Multiples categorias seran entregados en una lista de json, separados por comas ",
    operation_id="getTournaments",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_tournaments():
    tournaments = get_all_tournaments_db()
    return tournaments


@router.get(
    "/{id}",
    response_model=TournamentOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getTournament",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_tournament_id(id: str):
    tournament = get_tournament_id_db(id)
    return tournament


@router.post(
    "/",
    response_model=TournamentOut,
    status_code=200,
    summary="Cree una categoria",
    description="Cree una categoria enviando sus datos en un JSON",
    operation_id="createTournament",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_tournament(nuevo_tournament: TournamentIn):
    tournament = create_tournament_db(nuevo_tournament)
    return tournament
