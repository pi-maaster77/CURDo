from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from os import environ as env

DATABASE = env.get("DATABASE_URL") or "sqlite:///./test.db"
engine = create_engine(DATABASE)
Base = declarative_base()

# Importar las tablas para registrarlas en Base.metadata
from .models.elemento import Elemento
from .models.tag import Tag
from .models.tag_elemento import tag_elemento

# Crear todas las tablas
Base.metadata.create_all(engine)

