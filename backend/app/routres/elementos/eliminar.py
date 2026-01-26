from fastapi import APIRouter
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Elemento

router = APIRouter()

@router.delete("/eliminar")

async def eliminar_elementos(id:int):
    with Session(engine) as session:
        elemento = session.query(Elemento).filter(Elemento.id == id).first()
        if elemento is None:
            return {"message": "Elemento no encontrado"}
        session.delete(elemento)
        session.commit()
        return {"message": "Elemento eliminado", "id": id}