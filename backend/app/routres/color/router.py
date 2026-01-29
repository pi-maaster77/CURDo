from fastapi import APIRouter
from .listar import router as listar_router
from .crear import router as crear_router
from .editar import router as editar_router
from .eliminar import router as eliminar_router

router = APIRouter(tags=["Colores"])

router.include_router(listar_router)
router.include_router(crear_router)
router.include_router(editar_router)
router.include_router(eliminar_router)
