from fastapi import APIRouter, Depends
from backend.auth.rbac import verificar_permissao

router = APIRouter()

@router.get("/marketplace/concorrencia", dependencies=[Depends(verificar_permissao("marketplace"))])
def obter_concorrencia():
    return {
        "concorrentes_monitorados": 12,
        "anuncios_com_margem_critica": 4,
        "recomendacoes_ia": [
            "Revisar preço SKU010",
            "Substituir imagem SKU011",
            "Ativar anúncio SKU012"
        ]
    }