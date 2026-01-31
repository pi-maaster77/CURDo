from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag

class TagEditRequest(BaseModel):
    nombre: str

router = APIRouter()

@router.patch("/{id}")
async def editar_colors(id, color: TagEditRequest):
    if not color.nombre:
        return HTTPException(
            status_code=400,
            detail="Debe enviarse al menos un campo"
        )
    with Session(engine) as session:
        color_db = session.get(Tag, color.id)
        if color_db is None:
            raise HTTPException(
                status_code=404,
                detail="Tag no encontrada"
            )

        color_db.nombre = color.nombre

        try:
            session.commit()
            session.refresh(color_db)
            return {
                "message": "Tag editado correctamente",
                "id": color_db.id, 
                "nombre": color_db.nombre,
                "color": {
                    "nombre": color_db.color.nombre,
                    "id": color_db.color.id
                }
            }
    
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
