from fastapi import APIRouter
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag
router = APIRouter()

@router.get("/")
async def listar_tags():
    with Session(engine) as session:
        tags = session.query(Tag).all()
        resultado = []
        for tag in tags:
            resultado.append({
                "id": tag.id,
                "nombre": tag.nombre,
                "color": {
                    "id": tag.color.id,
                    "nombre": tag.color.nombre,
                    "rojo": tag.color.rojo,
                    "verde": tag.color.verde,
                    "azul": tag.color.azul,
                }
            })
        return resultado