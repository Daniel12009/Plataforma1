
from fastapi import APIRouter

router = APIRouter(prefix="/demo", tags=["DEMO"])

@router.get("/dados")
def dados_demo():
    return {
        "modo": "DEMO",
        "vendas_simuladas": 234,
        "lucro_estimado": 12345.67,
        "mensagem": "Esse é o modo demonstração do VixPanel"
    }
