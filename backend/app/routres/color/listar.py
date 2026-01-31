from fastapi import APIRouter
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Color
router = APIRouter()

@router.get("/")
async def listar_colors():
    with Session(engine) as session:
        colores = session.query(Color).all()
        resultado = []
        for color in colores:
            resultado.append({
                "id": color.id,
                "nombre": color.nombre,
                "rojo": color.rojo,
                "verde": color.verde,
                "azul": color.azul
            })
        return resultado