from fastapi import APIRouter, Depends
from backend.auth.rbac import verificar_permissao

router = APIRouter()

@router.get("/estoque/produtos", dependencies=[Depends(verificar_permissao("estoque"))])
def listar_produtos():
    return [
        {"sku": "SKU010", "nome": "Torneira Luxo", "estoque": 8},
        {"sku": "SKU011", "nome": "Chuveiro Redondo", "estoque": 15}
    ]