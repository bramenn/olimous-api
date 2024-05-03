from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_competitor_db, get_all_competitors_db, get_competitor_id_db
from .modelo import CompetitorIn, CompetitorOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[CompetitorOut],
    status_code=200,
    summary="Obtenga todas los competidores",
    description="Multiples competidores seran entregados en una lista de json, separados por comas ",
    operation_id="getCompetitors",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_competitors():
    competitors = get_all_competitors_db()
    return competitors


@router.get(
    "/{id}",
    response_model=CompetitorOut,
    status_code=200,
    summary="Obtenga un competidor por id",
    description="Una competidor sera entregada",
    operation_id="getCompetitor",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_competitor_id(id: str):
    competitor = get_competitor_id_db(id)
    return competitor


@router.post(
    "/",
    response_model=CompetitorOut,
    status_code=200,
    summary="Cree un competidor",
    description="Cree un competidor enviando sus datos en un JSON",
    operation_id="createCompetitor",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_competitor(nuevo_competitor: CompetitorIn):
    competitor = create_competitor_db(nuevo_competitor)
    return competitor
