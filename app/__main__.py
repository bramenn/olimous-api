import uvicorn
from fastapi import FastAPI

from .category import endpoint as category_endpoint
from .db import Base, conn
from .game import endpoint as game_endpoint
from .manager import endpoint as manager_endpoint

app = FastAPI()

app.include_router(category_endpoint.router, prefix="/v1/category", tags=["category"])
app.include_router(
    manager_endpoint.router,
    prefix="/v1/manager",
    tags=["manager"],
)


if __name__ == "__main__":
    Base.metadata.create_all(conn)
    uvicorn.run(app=app, host="0.0.0.0", port=80)
