from fastapi import APIRouter, Depends
from backend.auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/alertas", dependencies=[Depends(JWTBearer())])

@router.get("")
def listar_alertas():
    return {"alertas": ["Estoque baixo", "Margem negativa", "Anúncio pausado"]}