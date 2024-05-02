from pydantic import BaseModel


class _404NotFound(BaseModel):
    detail: str = "Recusro no encontrado"


class _409Conflict(BaseModel):
    detail: str


class _500ServerError(BaseModel):
    detail: str = "Error en el servidor"
