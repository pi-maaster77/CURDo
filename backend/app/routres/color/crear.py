from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Color

class ColorCreateRequest(BaseModel):
    nombre: str
    rojo: int
    verde: int
    azul: int

router = APIRouter()

@router.post("/")
async def crear_color(color: ColorCreateRequest):
    # Validate presence of required fields (Pydantic enforces types)
    if not color.nombre or color.rojo is None or color.verde is None or color.azul is None:
        return {"message": "Peticion de creacion de color incompleta.", "color": color}
    with Session(engine) as session:
        nuevo_color = Color(
            nombre=color.nombre, 
            rojo=color.rojo,
            verde=color.verde,
            azul=color.azul
        )
        session.add(nuevo_color)
        session.commit()
        return {
                "message": "Color Creado", 
                "id": nuevo_color.id,
                "nombre": nuevo_color.nombre,
                "rojo": nuevo_color.rojo,
                "verde": nuevo_color.verde,
                "azul": nuevo_color.azul
            }
    