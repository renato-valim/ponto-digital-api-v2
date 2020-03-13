from flask import Blueprint, request
from flask import jsonify
import json

from app.utils.utils import format_string, read_json_file, write_json_file
from app.modules.libs.viagem_lib import viagem_completa, registrar_viagem

from app.database.entities.Viagem import Viagem
from app.database.entities.Passageiro import Passageiro
from app.database.daos.ViagemDAO import ViagemDAO

from app.modules.libs.controlador_viagem import ControladorViagem


viagem = Blueprint("viagem", __name__)

@viagem.route('/viagem/planejar', methods=['POST'])
def planejar_viagem():
    try:
        origem = format_string(request.json['origem'])
        destino = format_string(request.json['destino'])
        passageiro = Passageiro.toObj(request.json['passageiro'])

        viagem = viagem_completa(origem, destino, passageiro)

        return jsonify({'viagem':viagem,'status':200})


    except Exception as e:
        return jsonify({'err': str(e), 'status': 500})

@viagem.route('/viagem/confirmar', methods=['POST'])
def confirmar_viagem():
    try:
        viagem = ViagemDAO.create(Viagem.toObj(request.json['viagem']))

        viagem._token = request.json['token']

        controlador = ControladorViagem(viagem)
        controlador.start()

        return jsonify({'viagem':viagem.toDict(), 'status':200})
    except Exception as e:
        e.with_traceback()
        return jsonify({'err': str(e), 'status': 500})

@viagem.route('/viagem/status', methods=['GET'])
def status_viagem():
    try:
        id = request.args['id']
        viagem = read_json_file('app/database/temp/viagem/viagem_{}/info.json'.format(id))

        return jsonify({'viagem':viagem, 'status':200})

    except Exception as e:
        return jsonify({'err':str(e), 'status':500})

@viagem.route('/viagem/cancelar', methods=['GET', 'DELETE'])
def cancelar_viagem():
    try:
        id = request.args['id']
        status = open('app/database/temp/viagem/viagem_{}/STATUS.txt'.format(id), 'w')
        status.write("CANCELADA")

        status.close()

        return jsonify({'status':200})
    except Exception as e:
        return jsonify({'err':str(e), 'status':500})