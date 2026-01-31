from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from ...database import engine
from ...models import Tag, tag_elemento

router = APIRouter()

@router.delete("/{id}")
async def eliminar_tag(id: int):
    with Session(engine) as session:
        tag = session.get(Tag, id)
        if not tag:
            raise HTTPException(404, "Tag no encontrado")

        usado = session.scalar(
            select(tag_elemento).where(tag_elemento.c.tag_id == id).limit(1)
        )

        if usado:
            raise HTTPException(
                409,
                "No se puede eliminar el tag: está asignado a elementos"
            )

        session.delete(tag)
        session.commit()
        return {"message": "Tag eliminado", "id": id}
