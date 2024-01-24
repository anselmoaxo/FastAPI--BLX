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
        self.db.refresh()     
        return db_pedido

    def listar(self):
        pedidos = self.db.query(models.Pedido).all()
        return pedidos