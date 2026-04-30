from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy.sql import func
from core.database import Base

class Movimentacao(Base):
  __tablename__ = "movimentacao"

  id = Column(Integer, primary_key=True, index=True)
  descricao = Column(String(255), nullable=False)
  valor = Column(Float, nullable=False)
  tipo = Column(String(50), nullable=False)
  categoria = Column(String(100), nullable=False)
  data_movimentacao = Column(Date, nullable=False)
  data_criacao = Column(DateTime(timezone=True), server_default=func.now())