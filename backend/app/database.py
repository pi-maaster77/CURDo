from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from os import environ as env

try:
    import dotenv
    dotenv.load_dotenv()
except ModuleNotFoundError:
    pass


DATABASE = env.get("DATABASE_URL")
engine = create_engine(DATABASE)
Base = declarative_base()

# Importar las tablas para registrarlas en Base.metadata
from .models.elemento import Elemento
from .models.tag import Tag
from .models.tag_elemento import tag_elemento
from .models.color import Color

# Crear todas las tablas
Base.metadata.create_all(engine)

# --- Lógica de Color por Defecto ---
def init_db():
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        # Verificar si ya existe el color por defecto (ej. ID 1 o nombre 'Gris')
        default_color = db.query(Color).filter_by(id=1).first()
        if not default_color:
            new_color = Color(id=1, nombre="Predeterminado", rojo=0, verde=0, azul=0)
            db.add(new_color)
            db.commit()
            print("Color por defecto creado con éxito.")
    except Exception as e:
        print(f"Error al inicializar: {e}")
        db.rollback()
    finally:
        db.close()

init_db()