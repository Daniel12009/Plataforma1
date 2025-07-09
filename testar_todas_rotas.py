import requests

BASE_URL = "http://localhost:8000"

# Credenciais de login
login_data = {
    "email": "admin@viaflix.com",
    "senha": "123456"
}

# Autenticação
login_response = requests.post(f"{BASE_URL}/login", json=login_data)
if login_response.status_code == 200:
    token = login_response.json().get("access_token")
    print("✅ Token obtido com sucesso!")
    headers = {"Authorization": f"Bearer {token}"}
else:
    print("❌ Falha no login.")
    print("Status:", login_response.status_code)
    print("Resposta:", login_response.text)
    exit()

# Rotas para testar
routes = [
    "/dashboard/kpis",
    "/dashboard/alertas",
    "/estoque/produtos",
    "/configuracoes/usuarios",
    "/marketplace/analise",
]

# Teste das rotas
for route in routes:
    print(f"🔍 Testando rota: {route}")
    response = requests.get(f"{BASE_URL}{route}", headers=headers)
    print(f"🔐 Status: {response.status_code}")
    try:
        print("🧾 Resposta:", response.json())
    except Exception as e:
        print("⚠️ Erro ao ler resposta:", str(e))
    print("-" * 40)