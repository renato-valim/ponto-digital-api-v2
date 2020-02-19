from flask import Blueprint, request
from flask import jsonify

from app.database.daos.PassageiroDAO import PassageiroDAO
from app.database.entities.Passageiro import Passageiro

passageiro = Blueprint('passageiro', __name__)


@passageiro.route("/passageiro/cadastrar", methods=['POST'])
def cadastrar_passageiro():
    try:
        novo_passageiro = Passageiro()

        novo_passageiro.nome = request.json['nome']
        novo_passageiro.nome_usuario = request.json['nome_usuario']
        novo_passageiro.rg = request.json['rg']
        novo_passageiro.cpf = request.json['cpf']
        novo_passageiro.data_nascimento = request.json['data_nascimento']
        novo_passageiro.endereco = request.json['endereco']
        novo_passageiro.genero = request.json['genero']
        novo_passageiro.tipo = request.json['tipo']
        novo_passageiro.senha = request.json['senha']

        PassageiroDAO.create(novo_passageiro)

        return jsonify({'status': 200})

    except Exception as e:
        return jsonify({'err': 'Erro na criação do passageiro: {}'.format(str(e)), 'status': 500})

@passageiro.route("/passageiro/login", methods=['POST'])
def login_passageiro():
    try:
        nome_usuario = request.json['nome_usuario']
        senha = request.json['senha']

        passageiro = PassageiroDAO.login(nome_usuario, senha)

        if(not(passageiro.id == None)):
            return jsonify({'status':200, 'passageiro':passageiro.toDict()})
        else:
            return jsonify({'status':500, 'err':'Credenciais Inválidas'})

    except Exception:
        return jsonify({'status':500, 'err':'Erro no Login, tente novamente'})