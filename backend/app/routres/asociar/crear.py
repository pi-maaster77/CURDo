from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ...database import engine
from ...models import tag_elemento, Elemento, Tag

router = APIRouter()

@router.post("/elementos/{elemento_id}/tags/{tag_id}")
async def asociar_tag(elemento_id: int, tag_id: int):
    with Session(engine) as session:
        elemento = session.get(Elemento, elemento_id)
        tag = session.get(Tag, tag_id)

        if not elemento or not tag:
            raise HTTPException(404, "Elemento o Tag no encontrado")

        if tag not in elemento.tags:
            elemento.tags.append(tag)

        session.commit()
        return {"message": "Tag asociado al elemento"}
