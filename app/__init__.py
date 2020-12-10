from flask import Flask
from blueprints.sneakers import bp as sneakers_bp
from blueprints.tshirts import bp as tshirts_bp
from blueprints.statictics import bp as stat_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(sneakers_bp, url_prefix='/sneakers')
    app.register_blueprint(tshirts_bp, url_prefix='/tshirts')
    app.register_blueprint(stat_bp, url_prefix='/statistics')
    return app


if __name__ == '__main__':
    create_app().run()

