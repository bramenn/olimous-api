import uvicorn
from fastapi import FastAPI

from .category import endpoint as category_endpoint
from .db import Base, conn
from .game import endpoint as game_endpoint
from .manager import endpoint as manager_endpoint

# from .responsable import endpoint as responsable_endpoint
# from .suscripcion import endpoint as suscripcion_endpoint

app = FastAPI()

# app.include_router(responsable_endpoint.router, prefix="/v1/responsable", tags=["responsable"])
app.include_router(
    manager_endpoint.router,
    prefix="/v1/manager",
    tags=["manager"],
)
# app.include_router(suscripcion_endpoint.router, prefix="/v1/suscripcion", tags=["suscripcion"])


if __name__ == "__main__":
    Base.metadata.create_all(conn)
    uvicorn.run(app=app, host="0.0.0.0", port=80)
