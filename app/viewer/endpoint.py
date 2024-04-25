from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_viewer_db, get_all_viewers_db, get_viewer_id_db
from .modelo import ViewerIn, ViewerOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[ViewerOut],
    status_code=200,
    summary="Obtenga todas las categorias",
    description="Multiples categorias seran entregados en una lista de json, separados por comas ",
    operation_id="getViewers",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_viewers():
    viewers = get_all_viewers_db()
    return viewers


@router.get(
    "/{id}",
    response_model=ViewerOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_viewer_id(id: str):
    viewer = get_viewer_id_db(id)
    return viewer


@router.post(
    "/",
    response_model=ViewerOut,
    status_code=200,
    summary="Cree una categoria",
    description="Cree una categoria enviando sus datos en un JSON",
    operation_id="createViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_viewer(nuevo_viewer: ViewerIn):
    viewer = create_viewer_db(nuevo_viewer)
    return viewer
