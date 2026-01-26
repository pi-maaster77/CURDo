from fastapi import APIRouter
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Elemento
router = APIRouter()

@router.get("/listar")
async def listar_elementos():
    with Session(engine) as session:
        elementos = session.query(Elemento).all()
        resultado = []
        for elemento in elementos:
            resultado.append({
                "id": elemento.id,
                "nombre": elemento.nombre,
                "checked": elemento.checked
            })
        return resultado