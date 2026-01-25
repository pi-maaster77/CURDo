from flask import Blueprint, jsonify
from ..database import engine
from ..tables.elemento import Elemento
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

bp = Blueprint("api", __name__)

@bp.route("/elementos", methods=["GET"], strict_slashes=False)
def obtener_elementos():
    with Session() as session:
        elementos = session.query(Elemento).all()
        resultado = [{"id": e.id, "nombre": e.nombre, "tick": e.tick} for e in elementos]
    return jsonify(resultado)

@bp.route("/elementos/<int:elemento_id>", methods=["GET"], strict_slashes=False)
def obtener_elemento(elemento_id):
    with Session() as session:
        elemento = session.get(Elemento, elemento_id)
        if elemento:
            resultado = {"id": elemento.id, "nombre": elemento.nombre, "tick": elemento.tick}
            return jsonify(resultado)
        else:
            return jsonify({"error": "Elemento no encontrado"}), 404

@bp.route("/elementos", methods=["POST"], strict_slashes=False)
def crear_elemento():
    from flask import request
    datos = request.get_json()
    nuevo_elemento = Elemento(nombre=datos["nombre"], tick=False)
    with Session() as session:
        session.add(nuevo_elemento)
        session.commit()
        resultado = {"id": nuevo_elemento.id, "nombre": nuevo_elemento.nombre, "tick": nuevo_elemento.tick}
    return jsonify(resultado), 201

@bp.route("/elementos/<int:elemento_id>", methods=["PUT"], strict_slashes=False)
def actualizar_elemento(elemento_id):
    from flask import request
    datos = request.get_json()
    with Session() as session:
        elemento = session.get(Elemento, elemento_id)
        if elemento:
            if "nombre" in datos:
                elemento.nombre = datos["nombre"]
            if "tick" in datos:
                elemento.tick = datos["tick"]
            session.commit()
            resultado = {"id": elemento.id, "nombre": elemento.nombre, "tick": elemento.tick}
            return jsonify(resultado)
        else:
            return jsonify({"error": "Elemento no encontrado"}), 404
        
@bp.route("/elementos/<int:elemento_id>", methods=["DELETE"], strict_slashes=False)
def eliminar_elemento(elemento_id):
    with Session() as session:
        elemento = session.get(Elemento, elemento_id)
        if elemento:
            session.delete(elemento)
            session.commit()
            return jsonify({"mensaje": "Elemento eliminado"})
        else:
            return jsonify({"error": "Elemento no encontrado"}), 404

@bp.route("/elementos/<int:elemento_id>", methods=["PATCH"], strict_slashes=False)
def toggle_tick(elemento_id):
    with Session() as session:
        elemento = session.get(Elemento, elemento_id)
        if elemento:
            elemento.tick = not elemento.tick
            session.commit()
            resultado = {"id": elemento.id, "nombre": elemento.nombre, "tick": elemento.tick}
            return jsonify(resultado)
        else:
            return jsonify({"error": "Elemento no encontrado"}), 404