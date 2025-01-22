from fastapi import APIRouter

from src.api.endpoints_v1.wallets import router as wallet_router

router = APIRouter(prefix="/api/v1/tron-service")

router.include_router(wallet_router, tags=["wallet"])
