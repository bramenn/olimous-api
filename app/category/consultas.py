from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..config import DEFAUL_FREE_LIMIT_PARTICIPANTS, DEFAUL_FREE_LIMIT_VIEWERS
from .modelo import Category, CategoryIn, CategoryOut


def get_all_categorys_db() -> CategoryOut:
    categorys = db.session.query(Category)

    if not categorys:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categorys no encontradas",
        )

    return [parse_category(category) for category in categorys]


def get_category_id_db(id: str) -> CategoryOut:
    category = db.session.query(Category).where(Category.id == id).first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category no encontrada",
        )

    return parse_category(category)


def create_category_db(
    new_category: CategoryIn,
) -> CategoryOut:
    category = Category(
        name=new_category.name,
        alias=new_category.alias,
        description=new_category.description,
        limit_viwers=new_category.limit_viwers
        if not new_category.is_free
        else DEFAUL_FREE_LIMIT_VIEWERS,
        limit_participants=new_category.limit_participants
        if not new_category.is_free
        else DEFAUL_FREE_LIMIT_PARTICIPANTS,
        comission=new_category.comission if not new_category.is_free else 0,
        is_free=new_category.is_free,
    )

    try:
        db.session.add(category)
        db.session.commit()
        return parse_category(category)
    except Exception as e:
        print("No se ha creado la category: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la category",
        )


def parse_category(category: Category) -> CategoryOut:
    return CategoryOut(
        id=category.id,
        name=category.name,
        alias=category.alias,
        description=category.description,
        limit_viwers=category.limit_viwers,
        limit_participants=category.limit_participants,
        commission=category.comission,
        is_free=category.is_free,
    )
