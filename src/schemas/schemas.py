from pydantic import BaseModel
from typing import List, Optional


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
   
    
class Produto(BaseModel):
    id: Optional[int] 
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False
    desconto: float
    id_usuario: int
    


    class Config:
        from_attributes = True

        
class Pedido(BaseModel):
    id: Optional[int] = None
    #usuario: Usuario
    #produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem Observacoes'
    
    