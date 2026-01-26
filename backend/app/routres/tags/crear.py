from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag

class TagsCreateRequest(BaseModel):
    nombre: str

router = APIRouter()

@router.post("/crear")
async def crear_tags(tag: TagsCreateRequest):
    if not tag.nombre:
        return {"message": "Nombre del tag es requerido"}
    with Session(engine) as session:
        nueva_tag = Tag(nombre=tag.nombre)
        session.add(nueva_tag)
        session.commit()
        return {"message": "Tag creado", "nombre": nueva_tag.nombre}
    

    