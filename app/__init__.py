from flask import Flask
from config import Config
from .extensions import db, migrate, jwt
from .routes.auth_routes import auth_bp
from .routes.item_routes import item_bp
from .routes.order_routes import order_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Registra Blueprints (rotas)
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(item_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')

    return app