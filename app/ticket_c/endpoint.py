from typing import List

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from ..responses.http import _404NotFound, _500ServerError
from .consultas import (
    create_ticket_competitor_db,
    get_all_ticket_competitors_db,
    get_ticket_competitor_id_db,
    get_ticket_competitor_qr_code_db,
)
from .modelo import TicketCompetitorIn, TicketCompetitorOut

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/",
    response_model=List[TicketCompetitorOut],
    status_code=200,
    summary="Obtenga todas las categorias",
    description="Multiples categorias seran entregados en una lista de json, separados por comas ",
    operation_id="getTicketCompetitors",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_ticket_competitors():
    ticket_competitors = get_all_ticket_competitors_db()
    return ticket_competitors


@router.get(
    "/{id}",
    response_model=TicketCompetitorOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getTicketCompetitor",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_competitor_id(id: str):
    ticket_competitor = get_ticket_competitor_id_db(id)
    return ticket_competitor


@router.get(
    "/read_qr/{qr_code}",
    response_model=TicketCompetitorOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getTicketCompetitor",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_ticket_competitor_id(qr_code: str):
    ticket_competitor = get_ticket_competitor_qr_code_db(qr_code)
    return ticket_competitor


@router.post(
    "/",
    response_model=TicketCompetitorOut,
    status_code=200,
    summary="Cree una categoria",
    description="Cree una categoria enviando sus datos en un JSON",
    operation_id="createTicketCompetitor",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_ticket_competitor(request: Request, nuevo_ticket_competitor: TicketCompetitorIn):
    ticket_competitor = create_ticket_competitor_db(nuevo_ticket_competitor)
    data = {
        "ticket_id": ticket_competitor.id,
        "tournament_name": ticket_competitor.tournament_id,
        "user_name": ticket_competitor.competitor_id,
        "qr_code_url": f"{request.url}read_qr/{ticket_competitor.qr_code}",
    }
    return templates.TemplateResponse("ticket_template.html", {"request": request, **data})
