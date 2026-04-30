from sqlalchemy.orm import Session
from repositories.movimentacao_repository import MovimentacaoRepository
from schemas.movimentacao import MovimentacaoCreate

class MovimentacaoService:

    @staticmethod
    def criar_movimentacao(db: Session, movimentacao_data: MovimentacaoCreate):
        return MovimentacaoRepository.create(db, movimentacao_data)

    @staticmethod
    def listar_movimentacoes(db: Session):
        return MovimentacaoRepository.get_all(db)