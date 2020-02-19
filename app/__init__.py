from flask import Flask

from app.modules.controllers.geolocalizacao import geolocalizacao
from app.modules.controllers.passageiro import passageiro
from app.modules.controllers.viagem import viagem


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(geolocalizacao)
    app.register_blueprint(passageiro)
    app.register_blueprint(viagem)

    return app
