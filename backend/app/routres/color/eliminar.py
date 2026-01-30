from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from ...database import engine
from ...models import Color, Tag

router = APIRouter()

@router.delete("/{id}")
async def eliminar_color(id: int):
    with Session(engine) as session:
        color = session.get(Color, id)
        if not color:
            raise HTTPException(404, "Color no encontrado")

        usados = session.scalar(
            select(Tag).where(Tag.color_id == id).limit(1)
        )

        if usados:
            raise HTTPException(
                409,
                "No se puede eliminar el color: está en uso por uno o más tags"
            )

        if color.id == 1:
            raise HTTPException(status_code=400, detail="No se puede eliminar el color por defecto.")
        session.delete(color)
        session.commit()

        return {"message": "Color eliminado", "id": id}
