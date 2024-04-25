import uvicorn
from fastapi import FastAPI

from .category import endpoint as category_endpoint
from .competitor import endpoint as competitor_endpoint
from .db import Base, conn
from .game import endpoint as game_endpoint
from .manager import endpoint as manager_endpoint
from .ticket_c import endpoint as ticket_c_endpoint
from .ticket_v import endpoint as ticket_v_endpoint
from .tournament import endpoint as tournament_endpoint
from .viewer import endpoint as viewer_endpoint

app = FastAPI()

app.include_router(category_endpoint.router, prefix="/v1/category", tags=["category"])
app.include_router(competitor_endpoint.router, prefix="/v1/competitor", tags=["competitor"])
app.include_router(game_endpoint.router, prefix="/v1/game", tags=["game"])
app.include_router(
    manager_endpoint.router,
    prefix="/v1/manager",
    tags=["manager"],
)
app.include_router(ticket_c_endpoint.router, prefix="/v1/ticket_c", tags=["ticket_c"])
app.include_router(ticket_v_endpoint.router, prefix="/v1/ticket_v", tags=["ticket_v"])
app.include_router(tournament_endpoint.router, prefix="/v1/tournament", tags=["tournament"])
app.include_router(viewer_endpoint.router, prefix="/v1/viewer", tags=["viewer"])


if __name__ == "__main__":
    Base.metadata.create_all(conn)
    uvicorn.run(app=app, host="0.0.0.0", port=80)
