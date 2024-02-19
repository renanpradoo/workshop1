from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"

class Vendas(BaseModel):
    email: str
    data: datetime
    valor: float
    produto: str
    quantidade: int
    categoria: str

