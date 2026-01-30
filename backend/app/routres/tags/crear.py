from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag

class TagsCreateRequest(BaseModel):
    nombre: str
    color: int

router = APIRouter()

@router.post("/")
async def crear_tags(tag: TagsCreateRequest):
    if not tag.nombre:
        return {"message": "Nombre del tag es requerido"}
    with Session(engine) as session:
        nueva_tag = Tag(nombre=tag.nombre, color_id=tag.color if tag.color else 1)
        session.add(nueva_tag)
        session.commit()
        return {"message": "Tag creado", 
                "nombre": nueva_tag.nombre, 
                "id": nueva_tag.id,
                "color": {
                    "id": nueva_tag.color.id,
                    "nombre": nueva_tag.color.nombre, 
                    "rojo": nueva_tag.color.rojo,
                    "verde": nueva_tag.color.verde,
                    "azul": nueva_tag.color.azul,
                }
                }
    

    