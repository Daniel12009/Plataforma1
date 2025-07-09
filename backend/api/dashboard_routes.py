
from fastapi import APIRouter, Depends
from backend.auth.rbac import verificar_token

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/kpis")
def obter_kpis(token: dict = Depends(verificar_token)):
    return {
        "total_vendas": 824,
        "faturamento_total": 73821.50,
        "ticket_medio": 89.56,
        "produtos_ativos": 157
    }

@router.get("/alertas")
def obter_alertas(token: dict = Depends(verificar_token)):
    return {
        "alertas": ["Estoque baixo", "Margem negativa", "Anúncio pausado"]
    }
