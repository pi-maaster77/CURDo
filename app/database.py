from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from os import environ as env

DATABASE = env.get("DATABASE_URL")
engine = create_engine(DATABASE)
Base = declarative_base()

# Importar las tablas para registrarlas en Base.metadata
from .tables import Elemento

# Crear todas las tablas
Base.metadata.create_all(engine)

