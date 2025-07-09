from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.models.user_model import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

router = APIRouter()

class UserCreateSchema(BaseModel):
    email: str
    senha: str
    permissoes: list

class UserUpdateSchema(BaseModel):
    email: str
    senha: str = None
    permissoes: list = None

@router.post("/users")
def criar_novo_usuario(data: UserCreateSchema):
    try:
        user = criar_usuario(data.email, data.senha, data.permissoes)
        return {"message": "Usuário criado com sucesso", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users")
def obter_usuarios():
    users = listar_usuarios()
    return {"users": users}

@router.put("/users/{user_id}")
def atualizar_usuario_existente(user_id: int, data: UserUpdateSchema):
    try:
        user = atualizar_usuario(user_id, data.email, data.senha, data.permissoes)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"message": "Usuário atualizado com sucesso", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/users/{user_id}")
def deletar_usuario_existente(user_id: int):
    success = deletar_usuario(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}

