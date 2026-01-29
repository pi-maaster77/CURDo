from sqlalchemy import Column, \
    Integer, \
    String, \
    ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from ..models.tag_elemento import tag_elemento

class Tag(Base):
    __tablename__="tag"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    elementos = relationship(
        "Elemento",
        secondary=tag_elemento,
        back_populates="tags"
    )

    color_id = Column(Integer, ForeignKey("color.id"))

    # 2. Creamos la conexión a nivel objeto Python
    color = relationship("Color", back_populates="tags")