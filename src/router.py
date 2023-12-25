from fastapi import APIRouter
from src.modules.sneakers import sneakers_router
from src.modules.core.main_router import router as main_router

def load_routers(app: APIRouter):
    app.include_router(main_router)
    app.include_router(sneakers_router)

    # Add other routers as needed
