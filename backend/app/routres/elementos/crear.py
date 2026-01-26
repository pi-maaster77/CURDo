from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Elemento

class ElementoCreateRequest(BaseModel):
    nombre: str

router = APIRouter()

@router.post("/crear")
async def crear_elementos(elemento: ElementoCreateRequest):
    if not elemento.nombre:
        return {"message": "Nombre del elemento es requerido"}
    with Session(engine) as session:
        nuevo_elemento = Elemento(nombre=elemento.nombre, checked=False)
        session.add(nuevo_elemento)
        session.commit()
        return {"message": "Elemento creado", "nombre": nuevo_elemento.nombre}
