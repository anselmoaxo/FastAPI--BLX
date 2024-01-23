from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: Produto):
        with self.db.begin():
            db_produto = models.Produto(id=produto.id,
                                        nome=produto.nome,  
                                        detalhe=produto.detalhe,
                                        preco=produto.preco, 
                                        disponivel=produto.disponivel)
            
            self.db.add(db_produto)
            self.db.commit()
            return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass