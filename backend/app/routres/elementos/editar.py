from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Elemento

class ElementoEditRequest(BaseModel):
    id: int
    nombre: Optional[str] = None
    checked: Optional[bool] = None

router = APIRouter()

@router.patch("/editar")
def editar_elementos(elemento: ElementoEditRequest):

    if elemento.nombre is None and elemento.checked is None:
        raise HTTPException(
            status_code=400,
            detail="Debe enviarse al menos un campo"
        )

    with Session(engine) as session:
        elemento_db = session.get(Elemento, elemento.id)

        if elemento_db is None:
            raise HTTPException(
                status_code=404,
                detail="Elemento no encontrado"
            )

        if elemento.nombre is not None:
            elemento_db.nombre = elemento.nombre

        if elemento.checked is not None:
            elemento_db.checked = elemento.checked

        try:
            session.commit()
            session.refresh(elemento_db)
            return {
                "message": "Elemento editado correctamente",
                "id": elemento_db.id
            }
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
