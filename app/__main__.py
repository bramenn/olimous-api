import uvicorn
from fastapi import FastAPI

from .activo_petrolero import endpoint as activo_petrolero_endpoint
from .db import Base, conn
from .evento_activo_petrolero import endpoint as evento_activo_petrolero_endpoint
from .responsable import endpoint as responsable_endpoint
from .suscripcion import endpoint as suscripcion_endpoint

app = FastAPI()

app.include_router(responsable_endpoint.router, prefix="/v1/responsable", tags=["responsable"])
app.include_router(
    activo_petrolero_endpoint.router,
    prefix="/v1/activo_petrolero",
    tags=["activo_petrolero"],
)
app.include_router(suscripcion_endpoint.router, prefix="/v1/suscripcion", tags=["suscripcion"])
app.include_router(
    evento_activo_petrolero_endpoint.router,
    prefix="/v1/evento_activo_petrolero",
    tags=["evento_activo_petrolero"],
)


if __name__ == "__main__":
    Base.metadata.create_all(conn)
    uvicorn.run(app=app, host="0.0.0.0", port=80)