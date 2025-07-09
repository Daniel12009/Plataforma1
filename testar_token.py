import requests
from backend.auth.auth_handler import create_access_token

# 1. Login e captura do token
login_url = "http://localhost:8000/login"
login_data = {
    "email": "admin@viaflix.com",
    "senha": "123456"
}
token = create_access_token({
    "sub": "admin@viaflix.com",
    "permissoes": ["admin", "vendedor", "estoque", "marketplace"]
})

print("TOKEN DE TESTE:\n", token)

login_response = requests.post(login_url, json=login_data)
if login_response.status_code != 200:
    print("Erro ao fazer login:", login_response.json())
    exit()

token = login_response.json()["access_token"]
print("✅ Token obtido com sucesso!")

# 2. Testar rota protegida
protected_url = "http://localhost:8000/dashboard/kpis"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(protected_url, headers=headers)

# 3. Resultado
print("🔐 Status:", response.status_code)
print("🧾 Resposta:", response.json())
