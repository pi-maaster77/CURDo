from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base
from .tag_elemento import tag_elemento

class Elemento(Base):
    __tablename__="elemento"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    checked = Column(Boolean)

    tags = relationship(
        "Tag",
        secondary=tag_elemento,
        back_populates="elementos"
    )