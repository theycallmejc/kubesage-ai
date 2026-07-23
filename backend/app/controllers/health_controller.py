from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/ready")
async def ready() -> dict[str, str]:
    return {"status": "ready", "timestamp": datetime.utcnow().isoformat()}

@router.get("/live")
async def live() -> dict[str, str]:
    return {"status": "live", "timestamp": datetime.utcnow().isoformat()}
