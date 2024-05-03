from typing import List

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from ..responses.http import _404NotFound, _409Conflict, _500ServerError
from .consultas import (
    block_qr_code_access,
    create_ticket_viewer_db,
    get_all_ticket_viewers_db,
    get_ticket_viewer_id_db,
    get_ticket_viewer_qr_code_db,
)
from .modelo import TicketViewerIn, TicketViewerOut

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/",
    response_model=List[TicketViewerOut],
    status_code=200,
    summary="Obtenga todos los tickets",
    description="Multiples tickets seran entregados en una lista de json, separados por comas ",
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
    summary="Obtenga un ticket por id",
    description="Una ticket sera entregada",
    operation_id="getTicketViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_viewer_id(id: str):
    ticket_viewer = get_ticket_viewer_id_db(id)
    return ticket_viewer


@router.get(
    "/read_qr/{qr_code}",
    response_model=TicketViewerOut,
    status_code=200,
    summary="Obtenga un ticket por qr",
    description="Un ticket sera entregada",
    operation_id="getTicketViewerQR",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_viewer_id(qr_code: str):
    ticket_viewer = get_ticket_viewer_qr_code_db(qr_code)
    return ticket_viewer


@router.get(
    "/block_access/{qr_code}",
    response_model=TicketViewerOut,
    status_code=200,
    summary="Bloquee un ticket por id",
    description="Un ticket sera bloqueado",
    operation_id="getBlockTicketViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_viewer_id(qr_code: str):
    blocked_ticket_viewer = block_qr_code_access(qr_code)
    return blocked_ticket_viewer


@router.get(
    "/unlock_access/{qr_code}",
    response_model=TicketViewerOut,
    status_code=200,
    summary="Debloquee un ticket por id",
    description="Un ticket sera desbloqueado",
    operation_id="getUnlockTicketViewer",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_viewer_id(qr_code: str):
    unlocked_ticket_viewer = block_qr_code_access(qr_code, True)
    return unlocked_ticket_viewer


@router.post(
    "/",
    response_model=TicketViewerOut,
    status_code=200,
    summary="Cree un ticket",
    description="Cree un ticket enviando sus datos en un JSON",
    operation_id="createTicketViewer",
    responses={
        404: {"model": _404NotFound},
        500: {"model": _500ServerError},
        409: {"model": _409Conflict},
    },
)
def create_ticket_viewer(request: Request, nuevo_ticket_viewer: TicketViewerIn):
    ticket_viewer = create_ticket_viewer_db(nuevo_ticket_viewer)
    data = {
        "ticket_id": ticket_viewer.id,
        "tournament_name": ticket_viewer.tournament_id,
        "user_name": ticket_viewer.viewer_id,
        "qr_code_url": f"{request.url}read_qr/{ticket_viewer.qr_code}",
        "total_price": ticket_viewer.total_price,
        "comission": ticket_viewer.commission,
    }
    return templates.TemplateResponse("ticket_template.html", {"request": request, **data})
