from fastapi import APIRouter
from app.modules.manufacturing.router import router as manufacturing_router
from app.modules.distribution.router import router as distribution_router
from app.modules.financial.router import router as financial_router

api_router = APIRouter()

api_router.include_router(manufacturing_router, prefix="/manufacturing", tags=["Manufacturing"])
api_router.include_router(distribution_router, prefix="/distribution", tags=["Distribution"])
api_router.include_router(financial_router, prefix="/financial", tags=["Financial"])
