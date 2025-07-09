from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Mock database para APIs
mock_apis_db = [
    {
        "id": 1,
        "nome": "API Mercado Livre",
        "url": "https://api.mercadolivre.com.br",
        "token": "MLM123456789",
        "status": "ativo",
        "descricao": "API para integração com Mercado Livre"
    },
    {
        "id": 2,
        "nome": "API Shopee",
        "url": "https://partner.shopeemobile.com",
        "token": "SHP987654321",
        "status": "inativo",
        "descricao": "API para integração com Shopee"
    }
]

class APICreateSchema(BaseModel):
    nome: str
    url: str
    token: str
    status: str = "ativo"
    descricao: Optional[str] = None

class APIUpdateSchema(BaseModel):
    nome: Optional[str] = None
    url: Optional[str] = None
    token: Optional[str] = None
    status: Optional[str] = None
    descricao: Optional[str] = None

@router.get("/apis")
def listar_apis():
    """Listar todas as APIs cadastradas"""
    return {"apis": mock_apis_db}

@router.post("/apis")
def criar_api(data: APICreateSchema):
    """Criar uma nova API"""
    try:
        # Gerar novo ID
        new_id = max([api["id"] for api in mock_apis_db]) + 1 if mock_apis_db else 1
        
        # Verificar se já existe uma API com o mesmo nome
        for api in mock_apis_db:
            if api["nome"].lower() == data.nome.lower():
                raise HTTPException(status_code=400, detail="Já existe uma API com este nome")
        
        # Criar nova API
        new_api = {
            "id": new_id,
            "nome": data.nome,
            "url": data.url,
            "token": data.token,
            "status": data.status,
            "descricao": data.descricao
        }
        
        mock_apis_db.append(new_api)
        return {"message": "API criada com sucesso", "api": new_api}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar API: {str(e)}")

@router.get("/apis/{api_id}")
def obter_api(api_id: int):
    """Obter uma API específica"""
    for api in mock_apis_db:
        if api["id"] == api_id:
            return {"api": api}
    raise HTTPException(status_code=404, detail="API não encontrada")

@router.put("/apis/{api_id}")
def atualizar_api(api_id: int, data: APIUpdateSchema):
    """Atualizar uma API existente"""
    for api in mock_apis_db:
        if api["id"] == api_id:
            # Verificar se o novo nome já existe em outra API
            if data.nome:
                for other_api in mock_apis_db:
                    if other_api["id"] != api_id and other_api["nome"].lower() == data.nome.lower():
                        raise HTTPException(status_code=400, detail="Já existe uma API com este nome")
                api["nome"] = data.nome
            
            if data.url:
                api["url"] = data.url
            if data.token:
                api["token"] = data.token
            if data.status:
                api["status"] = data.status
            if data.descricao is not None:
                api["descricao"] = data.descricao
            
            return {"message": "API atualizada com sucesso", "api": api}
    
    raise HTTPException(status_code=404, detail="API não encontrada")

@router.delete("/apis/{api_id}")
def deletar_api(api_id: int):
    """Deletar uma API"""
    for i, api in enumerate(mock_apis_db):
        if api["id"] == api_id:
            deleted_api = mock_apis_db.pop(i)
            return {"message": "API deletada com sucesso", "api": deleted_api}
    
    raise HTTPException(status_code=404, detail="API não encontrada")

@router.post("/apis/{api_id}/test")
def testar_api(api_id: int):
    """Testar conexão com uma API"""
    for api in mock_apis_db:
        if api["id"] == api_id:
            # Simulação de teste de API
            import random
            success = random.choice([True, False])
            
            if success:
                return {
                    "message": "Teste realizado com sucesso",
                    "status": "conectado",
                    "response_time": f"{random.randint(100, 500)}ms"
                }
            else:
                return {
                    "message": "Falha na conexão",
                    "status": "erro",
                    "error": "Timeout ou credenciais inválidas"
                }
    
    raise HTTPException(status_code=404, detail="API não encontrada")

