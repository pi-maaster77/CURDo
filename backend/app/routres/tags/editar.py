from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag

class TagEditRequest(BaseModel):
    nombre: Optional[str] = None
    color: Optional[int] = None

router = APIRouter()

@router.patch("/{id}")
async def editar_tags(id, tag: TagEditRequest):
    if not tag.nombre and not tag.color:
        raise HTTPException(
            status_code=400,
            detail="Debe enviarse al menos un campo"
        )
    with Session(engine) as session:
        tag_db = session.get(Tag, id)
        if tag_db is None:
            raise HTTPException(
                status_code=404,
                detail="Tag no encontrada"
            )


        if tag.nombre is not None:
            tag_db.nombre = tag.nombre

        if tag.color is not None:
            tag_db.color_id = tag.color

        try:
            session.commit()
            session.refresh(tag_db)
            return {
                "message": "Tag editado correctamente",
                "id": tag_db.id,
                "nombre": tag_db.nombre,
                "color": {
                    "id":tag_db.color.id,
                    "nombre":tag_db.color.nombre, 
                    "rojo":tag_db.color.rojo,
                    "verde":tag_db.color.verde,
                    "azul":tag_db.color.azul,
                }
            }
    
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
