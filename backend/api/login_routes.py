from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Usuario(BaseModel):
    email: str
    senha: str
    nome: str
    tipo: str

usuarios_demo = [
    Usuario(email="admin@vixpanel.com", senha="admin123", nome="Administrador", tipo="admin"),
    Usuario(email="supervisor@vixpanel.com", senha="super123", nome="Supervisor", tipo="supervisor"),
    Usuario(email="vendedor@vixpanel.com", senha="vend123", nome="Vendedor", tipo="vendedor"),
    Usuario(email="leitura@vixpanel.com", senha="leit123", nome="Usuário de Leitura", tipo="leitura")
]

@router.get("/users/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios_demo

@router.post("/users/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    usuarios_demo.append(usuario)
    return usuario
