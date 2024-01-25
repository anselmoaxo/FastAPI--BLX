from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(id=produto.id,
                                    nome=produto.nome,  
                                    detalhe=produto.detalhe,
                                    preco=produto.preco, 
                                    disponivel=produto.disponivel,
                                    desconto=produto.desconto,
                                    id_usuario=produto.id_usuario)
            
        self.db.add(db_produto)
        self.db.commit()   
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self, produto_id: int):
        produto = self.db.query(models.Produto).filter_by(id=produto_id).one()
        return produto
    
    def remover(self, produto_id: int):
        try:
            # Tenta remover o produto com o ID especificado
            self.db.query(models.Produto).filter_by(id=produto_id).delete()
            self.db.commit()
        except Exception as e:
            # Lida com exceções, por exemplo, se o produto não existir
            self.db.rollback()
            print(f"Erro ao remover produto: {e}")
            
        


        
