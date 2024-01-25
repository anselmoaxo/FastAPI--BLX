from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(id=usuario.id,
                                    nome=usuario.nome,
                                    senha=usuario.senha,
                                    telefone=usuario.telefone)
            
        self.db.add(db_usuario)
        self.db.commit()   
        return db_usuario

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios
    
    def obter(self, usuario_id: int):
        usuario = self.db.query(models.Usuario).filter_by(id=usuario_id).one()
        return usuario
    
    def remover(self, usuario_id: int):
        try:
            # Tenta remover o produto com o ID especificado
            self.db.query(models.Usuario).filter_by(id=usuario_id).delete()
            self.db.commit()
        except Exception as e:
            # Lida com exceções, por exemplo, se o produto não existir
            self.db.rollback()
            print(f"Erro ao remover Usuario: {e}")
            