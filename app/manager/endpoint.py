from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_manager_db, get_all_managers_db, get_manager_id_db
from .modelo import ManagerIn, ManagerOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[ManagerOut],
    status_code=200,
    summary="Obtenga todos los organizadores",
    description="Multiples organizadores seran entregados en una lista de json, separados por comas ",
    operation_id="getManagers",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_managers():
    managers = get_all_managers_db()
    return managers


@router.get(
    "/{id}",
    response_model=ManagerOut,
    status_code=200,
    summary="Obtenga un responsable por id",
    description="Un organizador sera entregado",
    operation_id="getManager",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_manager_id(id: str):
    manager = get_manager_id_db(id)
    return manager


@router.post(
    "/",
    response_model=ManagerOut,
    status_code=200,
    summary="Cree un organizador",
    description="Cree un organizador enviando sus datos en un JSON",
    operation_id="createManager",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_manager(nuevo_manager: ManagerIn):
    manager = create_manager_db(nuevo_manager)
    return manager
