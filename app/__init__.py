from flask import Flask

from app.modules.controllers.geolocalizacao import geolocalizacao
from app.modules.controllers.passageiro import passageiro
from app.modules.controllers.viagem import viagem
import firebase_admin
from firebase_admin import credentials


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    cred = credentials.Certificate(
        "app/utils/firebase/credentials/pontodigital-504cd-firebase-adminsdk-916cl-9d0917a9b0.json")
    default_app = firebase_admin.initialize_app(cred)

    app.register_blueprint(geolocalizacao)
    app.register_blueprint(passageiro)
    app.register_blueprint(viagem)

    return app
