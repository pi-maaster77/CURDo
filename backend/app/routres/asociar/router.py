from fastapi import APIRouter
from .crear import router as crear_router
from .eliminar import router as eliminar_router

router = APIRouter(tags=["Asociar"])

router.include_router(crear_router)
router.include_router(eliminar_router)
