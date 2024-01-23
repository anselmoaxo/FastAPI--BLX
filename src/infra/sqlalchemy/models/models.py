from sqlalchemy import Column, Float, String, Integer, Boolean
from src.infra.sqlalchemy.config.database import Base


class Produto():

    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30))
    detalhe = Column(String(50))
    preco = Column(Float)
    disponivel = Column(Boolean)