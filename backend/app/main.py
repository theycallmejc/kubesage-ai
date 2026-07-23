from fastapi import FastAPI
from app.controllers.health_controller import router as health_router

app = FastAPI(
    title="KubeSage AI Backend",
    description="Infrastructure-first Kubernetes platform operations API",
    version="0.1.0",
)

app.include_router(health_router, prefix="/health")

@app.on_event("startup")
async def startup_event() -> None:
    pass
