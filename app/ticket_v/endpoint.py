from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_ticket_viewer_db, get_all_ticket_viewers_db, get_ticket_viewer_id_db
from .modelo import TicketViewerIn, TicketViewerOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[TicketViewerOut],
    status_code=200,
    summary="Obtenga todas las categorias",
    description="Multiples categorias seran entregados en una lista de json, separados por comas ",
    operation_id="getTicketViewers",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_ticket_viewers():
    ticket_viewers = get_all_ticket_viewers_db()
    return ticket_viewers


@router.get(
    "/{id}",
    response_model=TicketViewerOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getTicketViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_viewer_id(id: str):
    ticket_viewer = get_ticket_viewer_id_db(id)
    return ticket_viewer


@router.post(
    "/",
    response_model=TicketViewerOut,
    status_code=200,
    summary="Cree una categoria",
    description="Cree una categoria enviando sus datos en un JSON",
    operation_id="createTicketViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_ticket_viewer(nuevo_ticket_viewer: TicketViewerIn):
    ticket_viewer = create_ticket_viewer_db(nuevo_ticket_viewer)
    return ticket_viewer
