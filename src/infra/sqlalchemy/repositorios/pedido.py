from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(id=pedido.id,
                                  quantidade=pedido.quantidade, 
                                  entrega=pedido.entrega,
                                  endereco=pedido.endereco,
                                  observacoes=pedido.observacoes)
            
        self.db.add(db_pedido)
        self.db.commit()    
        return db_pedido

    def listar(self):
        pedidos = self.db.query(models.Pedido).all()
        return pedidos
    
    def obter(self, pedido_id: int):
        pedido = self.db.query(models.Pedido).filter_by(id=pedido_id).one()
        return pedido
    
    def remover(self, pedido_id: int):
        try:
            # Tenta remover o produto com o ID especificado
            self.db.query(models.Pedido).filter_by(id=pedido_id).delete()
            self.db.commit()
        except Exception as e:
            # Lida com exceções, por exemplo, se o produto não existir
            self.db.rollback()
            print(f"Erro ao remover Pedido: {e}")