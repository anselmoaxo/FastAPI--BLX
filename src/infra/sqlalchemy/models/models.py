from pydantic import BaseModel
from typing import List, Optional


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List['Produto']
    meus_pedidos: List['Pedido']
    minhas_vendas: List['Pedido'pip]
    
    
class Produto(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
    
    
class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes = Optional[str] = 'Sem Observacoes'
    
    