from sqlalchemy.orm import Session
from models.movimentacao import Movimentacao
from schemas.movimentacao import MovimentacaoCreate

class MovimentacaoRepository:
    
    @staticmethod
    def create(db: Session, movimentacao_data: MovimentacaoCreate) -> Movimentacao:
        db_movimentacao = Movimentacao(
            descricao=movimentacao_data.descricao,
            valor=movimentacao_data.valor,
            tipo=movimentacao_data.tipo,
            categoria=movimentacao_data.categoria,
            data_movimentacao=movimentacao_data.data_movimentacao
        )
        
        db.add(db_movimentacao)     
        db.commit()             
        db.refresh(db_movimentacao) 
        return db_movimentacao

    @staticmethod
    def get_all(db: Session):
        return db.query(Movimentacao).all()