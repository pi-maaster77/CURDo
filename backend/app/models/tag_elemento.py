from sqlalchemy import Table, Column, Integer, ForeignKey
from ..database import Base

tag_elemento = Table(
    "tag_elemento",
    Base.metadata,
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
    Column("elemento_id", ForeignKey("elemento.id"), primary_key=True)
)
