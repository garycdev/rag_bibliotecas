from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuración opcional
    app.config.from_object("app.config")

    # Importar y registrar blueprints (rutas)
    from app.routes.main_routes import main
    from app.routes.chat_routes import chat

    app.register_blueprint(main, url_prefix="/api/")
    app.register_blueprint(chat, url_prefix="/api/chat")

    return app
