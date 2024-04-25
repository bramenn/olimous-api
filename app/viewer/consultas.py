from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Viewer, ViewerIn, ViewerOut


def get_all_viewers_db() -> ViewerOut:
    viewers = db.session.query(Viewer)

    if not viewers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Viewers no encontradas",
        )

    return [parse_viewer(viewer) for viewer in viewers]


def get_viewer_id_db(id: str) -> ViewerOut:
    viewer = db.session.query(Viewer).where(Viewer.id == id).first()

    if not viewer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Viewer no encontrada",
        )

    return parse_viewer(viewer)


def create_viewer_db(
    new_viewer: ViewerIn,
) -> ViewerOut:
    viewer = Viewer(
        name=new_viewer.name,
        email=new_viewer.email,
        alias=new_viewer.alias,
        phone=new_viewer.phone,
    )

    try:
        db.session.add(viewer)
        db.session.commit()
        return parse_viewer(viewer)
    except Exception as e:
        print("No se ha creado la viewer: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la viewer",
        )


def parse_viewer(viewer: Viewer) -> ViewerOut:
    return ViewerOut(
        id=viewer.id,
        name=viewer.name,
        email=viewer.email,
        alias=viewer.alias,
        phone=viewer.phone,
    )
