from flask import Flask
from .routes import main
from .routes import elementos

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",  # <- le dice dónde buscar los HTML
        static_folder="../static"       # <- si tienes archivos estáticos
    )

    # Registrar blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(elementos.bp)

    return app