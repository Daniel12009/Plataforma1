from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import user_routes
from backend.api import login_routes, user_routes, api_routes
from backend.api import (
    dashboard_routes,
    alertas_routes,
    estoque_routes,
    configuracoes_routes,
    marketplace_routes,
    demo_routes,
)
from backend.api.concorrencia_routes import router as concorrencia_router
from backend.api.estoque_routes import router as estoque_router

app = FastAPI(title="VixPanel API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro das rotas
app.include_router(user_routes.router)
app.include_router(login_routes.router)
app.include_router(user_routes.router, prefix="/api")
app.include_router(api_routes.router, prefix="/api")
app.include_router(dashboard_routes.router, prefix="/dashboard")
app.include_router(alertas_routes.router, prefix="/dashboard")
app.include_router(estoque_routes.router, prefix="/estoque")
app.include_router(configuracoes_routes.router, prefix="/configuracoes")
app.include_router(marketplace_routes.router, prefix="/marketplace")
app.include_router(demo_routes.router)
app.include_router(concorrencia_router)
app.include_router(estoque_router)