from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from ..database import Base

class Elemento(Base):
    __tablename__="elemento"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tick = Column(Boolean)
