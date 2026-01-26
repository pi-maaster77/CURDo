from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag

class TagEditRequest(BaseModel):
    id: int
    nombre: str

router = APIRouter()

@router.patch("/editar")
async def editar_elementos(elemento: TagEditRequest):
    if not elemento.nombre:
        return HTTPException(
            status_code=400,
            detail="Debe enviarse al menos un campo"
        )
    with Session(engine) as session:
        tag_db = session.get(Tag, elemento.id)
        if tag_db is None:
            raise HTTPException(
                status_code=404,
                detail="Tag no encontrada"
            )

        tag_db.nombre = elemento.nombre

        try:
            session.commit()
            session.refresh(tag_db)
            return {
                "message": "Tag editado correctamente",
                "id": tag_db.id
            }
    
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
