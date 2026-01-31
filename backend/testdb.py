from app.database import engine
from sqlalchemy import inspect
from app.models.elemento import Elemento
from app.models.tag import Tag
from app.models.tag_elemento import tag_elemento

inspector = inspect(engine)
print("Tablas en la base de datos:")
for table_name in inspector.get_table_names():
    print(table_name)

print("\nColumnas en la tabla 'elemento':")
columns = inspector.get_columns('elemento')
for column in columns:
    print(f"{column['name']} - {column['type']}")
print("\nColumnas en la tabla 'tag':")
columns = inspector.get_columns('tag')
for column in columns:
    print(f"{column['name']} - {column['type']}")
print("\nColumnas en la tabla 'tag_elemento':")
columns = inspector.get_columns('tag_elemento')
for column in columns:
    print(f"{column['name']} - {column['type']}") 

# Verificar relaciones
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
with Session() as session:
    elemento = session.query(Elemento).first()
    if elemento:
        print(f"\nPrimer elemento: {elemento.nombre}")
        print("Tags asociados:")
        for tag in elemento.tags:
            print(f"- {tag.nombre}")
    else:
        print("\nNo hay elementos en la base de datos.")

# Crear 3 elementos y 4 etiquetas de prueba
with Session() as session:
    with session.begin():
        tag1 = Tag(nombre="Tag 1")
        tag2 = Tag(nombre="Tag 2")
        tag3 = Tag(nombre="Tag 3")
        tag4 = Tag(nombre="Tag 4")
        session.add_all([tag1, tag2, tag3, tag4])

        elemento1 = Elemento(nombre="Elemento de prueba", checked=False, tags=[tag1, tag2])
        elemento2 = Elemento(nombre="Elemento 2", checked=True, tags=[tag3])
        elemento3 = Elemento(nombre="Elemento 3", checked=False, tags=[tag2, tag4])
        session.add_all([elemento1, elemento2, elemento3])

# Verificar la creación
with Session() as session:
    elementos = session.query(Elemento).all()
    for elemento in elementos:
        print(f"\nVerificación - Elemento: {elemento.nombre}")
        for tag in elemento.tags:
            print(f"- Tag asociado: {tag.nombre}")

# Mostrar elementos con tag 2
with Session() as session:
    tag2 = session.query(Tag).filter_by(nombre="Tag 2").first()
    if tag2:
        print(f"\nElementos con '{tag2.nombre}':")
        for elemento in tag2.elementos:
            print(f"- {elemento.nombre}")
    else:
        print("\nTag 2 no encontrado.")
