from pydantic import BaseModel
from typing import List, Optional


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
   
    
class Produto(BaseModel):
    id: int
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
    
    class Config:
        from_attributes = True

        
class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    #produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem Observacoes'
    
    