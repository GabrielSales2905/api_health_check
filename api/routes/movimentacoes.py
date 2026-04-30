from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas.movimentacao import MovimentacaoCreate, MovimentacaoResponse
from services.movimentacao_service import MovimentacaoService
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=MovimentacaoResponse, status_code=status.HTTP_201_CREATED)
def criar_movimentacao(
    movimentacao: MovimentacaoCreate, 
    db: Session = Depends(get_db)
):
    return MovimentacaoService.criar_movimentacao(db, movimentacao)

@router.get("/", response_model=List[MovimentacaoResponse])
def listar_movimentacoes(db: Session = Depends(get_db)):
    return MovimentacaoService.listar_movimentacoes(db)