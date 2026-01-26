from fastapi import APIRouter
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Tag
router = APIRouter()

@router.get("/listar")
async def listar_elementos():
    with Session(engine) as session:
        tags = session.query(Tag).all()
        resultado = []
        for tag in tags:
            resultado.append({
                "id": tag.id,
                "nombre": tag.nombre,
            })
        return {"tags": resultado}