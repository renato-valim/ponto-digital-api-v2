from flask import Blueprint, request
from flask import jsonify

from app.utils.utils import format_string
from app.modules.libs.viagem_lib import viagem_completa

from app.database.entities.Viagem import Viagem


viagem = Blueprint("viagem", __name__)

@viagem.route('/viagem/planejar', methods=['GET'])
def planejar_viagem():
    try:
        origem = format_string(request.args['origem'])
        destino = format_string(request.args['destino'])

        viagem = viagem_completa(origem, destino)

        return jsonify({'viagem':viagem,'status':200})


    except Exception as e:
        return jsonify({'err': str(e), 'status': 500})