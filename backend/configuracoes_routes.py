
from fastapi import APIRouter, Depends
from backend.auth.rbac import verificar_token

router = APIRouter(prefix="/configuracoes", tags=["Configurações"])

@router.get("/usuarios")
def listar_usuarios(token: dict = Depends(verificar_token)):
    return [
        {"id": 1, "nome": "Admin", "email": "admin@viaflix.com", "permissao": ["admin", "vendedor"]},
        {"id": 2, "nome": "Vendedor", "email": "vendedor@viaflix.com", "permissao": ["vendedor"]}
    ]
