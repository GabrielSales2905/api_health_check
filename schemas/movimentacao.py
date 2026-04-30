from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, date
from typing import Literal

class MovimentacaoBase(BaseModel):
    descricao: str = Field(..., min_length=3, max_length=255)
    valor: float = Field(..., gt=0, description="O valor deve ser maior que zero")
    tipo: Literal["entrada", "saida"]
    categoria: str = Field(..., min_length=3, max_length=100)
    data_movimentacao: date

class MovimentacaoCreate(MovimentacaoBase):
    pass 

class MovimentacaoResponse(MovimentacaoBase):
    id: int
    data_criacao: datetime

    model_config = ConfigDict(from_attributes=True)