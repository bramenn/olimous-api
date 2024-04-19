from pydantic import BaseModel


class _404NotFound(BaseModel):
    detail: str = "Recusro no encontrado"


class _500ServerError(BaseModel):
    detail: str = "Error en el servidor"
