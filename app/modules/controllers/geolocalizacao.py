from flask import Blueprint, request
from flask import jsonify

from app.api.core_api import geocodificar_endereco, geocodificar_coordenadas
from app.utils.utils import format_string

geolocalizacao = Blueprint('geolocalizacao', __name__)


@geolocalizacao.route("/viagem/origem", methods=['GET'])
def origem_handler():
    """
    Rota que recebe as coordenadas do usuário e retorna o endereço formatado
    """
    try:
        lat = request.args['lat']
        lng = request.args['lng']

        return jsonify({'status': 200, 'origem': geocodificar_coordenadas(lat, lng)['results'][0]['formatted_address']})

    except Exception as e:
        return jsonify({'err': str(e), 'status': 500})


@geolocalizacao.route("/viagem/destino", methods=['GET'])
def destino_handler():
    """
    Rota que recebe o destino do usuário e retorna o endereço formatado
    """

    try:
        destiny = request.args['destiny']

        formatted_destiny = format_string(destiny)

        return jsonify({'status': 200, 'destino': geocodificar_endereco("{0}, Indaiatuba".format(formatted_destiny))['results'][0]['formatted_address']})

    except Exception as e:
        return jsonify({'err': str(e), 'status': 500})
