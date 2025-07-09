
from fastapi import APIRouter, Depends
from backend.auth.rbac import verificar_token

router = APIRouter(prefix="/marketplace", tags=["Marketplace"])

@router.get("/analise")
def analise_marketplace(token: dict = Depends(verificar_token)):
    return {
        "concorrentes_monitorados": 18,
        "anuncios_com_margem_critica": 5,
        "recomendacoes_ia": ["Ajustar preço SKU002", "Melhorar imagem SKU005"]
    }
