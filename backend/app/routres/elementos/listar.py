from fastapi import APIRouter, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from ...database import engine
from ...models import Elemento, Tag
router = APIRouter()

@router.get("/")
def listar_elementos(
    tag: list[int] | None = Query(None),
    tag_mode: str = Query("any", regex="^(any|all)$"),
    checked: bool | None = None
):
    with Session(engine) as session:
        q = session.query(Elemento)

        # Tags
        if tag:
            if tag_mode == "all":
                for tag_id in tag:
                    q = q.filter(Elemento.tags.any(Tag.id == tag_id))
            else:
                q = q.filter(Elemento.tags.any(Tag.id.in_(tag)))

        # Checked
        if checked is not None:
            q = q.filter(Elemento.checked == checked)

        elementos = q.all()

        return [
            {
                "id": e.id,
                "nombre": e.nombre,
                "checked": e.checked,
                "tags": [t.id for t in e.tags],
            }
            for e in elementos
        ]
