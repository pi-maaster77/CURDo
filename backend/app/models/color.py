from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Color(Base):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    rojo = Column(Integer, nullable=False)
    verde = Column(Integer, nullable=False)
    azul = Column(Integer, nullable=False)

    # Relación: Permite hacer 'color.tags' para ver todos los tags de ese color
    tags = relationship("Tag", back_populates="color")