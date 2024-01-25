from fastapi import FastAPI, Depends, HTTPException, status
from src.schemas.schemas import Produto, Usuario, Pedido
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido

# criar_bd()

app = FastAPI(title='API Vendas', debug=True)



# PRODUTOS

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    try:
        produto_criado = RepositorioProduto(db).criar(produto)
        return produto_criado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@app.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
 
@app.get('/produtos/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(produto_id)
    return produto

@app.delete('/produtos/{produto_id}')
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(produto_id)
    return {'mensagem': f'Exclusão realizada do ID: {produto_id} '}



# USUARIOS
@app.post('/usuarios',status_code=status.HTTP_201_CREATED)
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios',status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@app.get('/usuarios/{usuario_id}')
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).obter(usuario_id)
    return usuario

@app.delete('/usuarios/{usuario_id}')
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(usuario_id)
    return {'mensagem': f'Exclusão realizada do ID: {usuario_id} '}



# PEDIDOS
@app.post('/pedidos',status_code=status.HTTP_201_CREATED)
def criar_pedidos(pedido: Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    return pedido_criado

@app.get('/pedidos',status_code=status.HTTP_200_OK)
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos

@app.get('/pedidos/{pedido_id}')
def obter_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = RepositorioPedido(db).obter(pedido_id)
    return pedido

@app.delete('/pedidos/{pedido_id}')
def remover_pedido(pedido_id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(pedido_id)
    return {'mensagem': f'Exclusão realizada do ID: {pedido_id} '}
