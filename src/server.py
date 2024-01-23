from fastapi import FastAPI, Depends, HTTPException
from src.schemas.schemas import Produto
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_bd()

app = FastAPI()


@app.post('/produtos')
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    try:
        produto_criado = RepositorioProduto.criar(produto, db)
        return produto_criado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


