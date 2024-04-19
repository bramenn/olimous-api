from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Manager, ManagerIn, ManagerOut


def get_all_managers_db() -> ManagerOut:
    managers = db.session.query(Manager)

    if not managers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Managers no encontradas",
        )

    return [parse_manager(manager) for manager in managers]


def get_manager_id_db(id: str) -> ManagerOut:
    manager = db.session.query(Manager).where(Manager.id == id).first()

    if not manager:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Manager no encontrado",
        )

    return parse_manager(manager)


def create_manager_db(
    nueva_manager: ManagerIn,
) -> ManagerOut:
    manager = Manager(
        name=nueva_manager.name,
        email=nueva_manager.email,
        phone=nueva_manager.phone,
    )

    try:
        db.session.add(manager)
        db.session.commit()
        return parse_manager(manager)
    except Exception as e:
        print("No se ha creado el manager: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el manager",
        )


def parse_manager(manager: Manager) -> ManagerOut:
    return ManagerOut(
        id=manager.id,
        name=manager.name,
        email=manager.email,
        phone=manager.phone,
    )
