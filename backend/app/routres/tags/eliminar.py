from fastapi import APIRouter
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag

router = APIRouter()

@router.delete("/eliminar")

async def eliminar_elementos(id:int):
    with Session(engine) as session:
        tag = session.query(Tag).filter(Tag.id == id).first()
        if tag is None:
            return {"message": "Tag no encontrado"}
        session.delete(tag)
        session.commit()
        return {"message": "Tag eliminado", "id": id}