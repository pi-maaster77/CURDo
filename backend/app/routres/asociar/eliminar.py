from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ...database import engine
from ...models import tag_elemento, Elemento, Tag

router = APIRouter()

@router.delete("/elementos/{elemento_id}/tags/{tag_id}")
async def quitar_tag(elemento_id: int, tag_id: int):
    with Session(engine) as session:
        elemento = session.get(Elemento, elemento_id)
        tag = session.get(Tag, tag_id)

        if not elemento or not tag:
            raise HTTPException(404)

        if tag in elemento.tags:
            elemento.tags.remove(tag)

        session.commit()
        return {"message": "Tag desasociado del elemento"}

