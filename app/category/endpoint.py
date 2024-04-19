from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_category_db, get_all_categorys_db, get_category_id_db
from .modelo import CategoryIn, CategoryOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[CategoryOut],
    status_code=200,
    summary="Obtenga todas las categorias",
    description="Multiples categorias seran entregados en una lista de json, separados por comas ",
    operation_id="getCategorys",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_categorys():
    categorys = get_all_categorys_db()
    return categorys


@router.get(
    "/{id}",
    response_model=CategoryOut,
    status_code=200,
    summary="Obtenga una categoria por id",
    description="Una categoria sera entregada",
    operation_id="getCategory",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_category_id(id: str):
    category = get_category_id_db(id)
    return category


@router.post(
    "/",
    response_model=CategoryOut,
    status_code=200,
    summary="Cree una categoria",
    description="Cree una categoria enviando sus datos en un JSON",
    operation_id="createCategory",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_category(nuevo_category: CategoryIn):
    category = create_category_db(nuevo_category)
    return category
