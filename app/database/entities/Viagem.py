from app.database.entities.Ponto import Ponto
from app.database.entities.Passageiro import Passageiro
from app.database.entities.Ponto import Ponto

from app.utils.utils import current_date

class Viagem:
    def __init__(
            self, 
            id = None, 
            origem = Ponto(), 
            destino = Ponto(),
            horario_partida = None,
            horario_chegada = None,
            passageiro = Passageiro(),
            status = None,
            minutos_restantes = None,
            linha_nome = None,
            linha_numero = None,
            letreiro = None,
            fase_da_viagem = None,
            viagem_id = None,
            token = None,
            veiculo = None,
            data = current_date()):

        self._id = id
        self._origem = origem
        self._destino = destino
        self._horario_partida = horario_partida
        self._horario_chegada = horario_chegada
        self._passageiro = passageiro
        self._status = status
        self._minutos_restantes = minutos_restantes
        self._linha_nome = linha_nome
        self._linha_numero = linha_numero
        self._letreiro = letreiro
        self._viagem_id = viagem_id
        self._data = data
        self._fase_da_viagem = fase_da_viagem
        self._token = token
        self._veiculo = veiculo
    

    @staticmethod
    def toObj(dict):
        passageiro = Passageiro.toObj(dict['passageiro'])
        origem = Ponto.toObj(dict['origem'])
        destino = Ponto.toObj(dict['destino'])

        viagem = Viagem()

        viagem._passageiro = passageiro
        viagem._origem = origem
        viagem._destino = destino

        viagem._horario_chegada = dict['horario_chegada']
        viagem._horario_partida = dict['horario_partida']
        viagem._letreiro = dict['letreiro']
        viagem._linha_nome = dict['linha_nome']
        viagem._linha_numero = dict['linha_numero']
        viagem._viagem_id = dict['viagem_id']
        viagem._id = dict['id']
        viagem._minutos_restantes = dict['minutos_restantes']
        viagem._data = dict['data']
        viagem._status = dict['status']
        viagem._token = dict['token']
        viagem._veiculo = dict['veiculo']
        viagem._fase_da_viagem = dict['fase_da_viagem']

        return viagem
        
    def toDict(self):
        return {
            "id":self._id,
            "origem":self._origem.toDict(),
            "destino":self._destino.toDict(),
            "horario_partida":self._horario_partida,
            "horario_chegada":self._horario_chegada,
            "passageiro":self._passageiro.toDict(),
            "status":self._status,
            "minutos_restantes":self._minutos_restantes,
            "linha_nome":self._linha_nome,
            "linha_numero":self._linha_numero,
            "letreiro":self._letreiro,
            "viagem_id":self._viagem_id,
            "data":self._data,
            "token":self._token,
            "veiculo":self._veiculo,
            "fase_da_viagem":self._fase_da_viagem
        }
    
    @property
    def fase_da_viagem(self):
        return self._fase_da_viagem
    
    @fase_da_viagem.setter
    def fase_da_viagem(self, fase_da_viagem):
        self._fase_da_viagem = fase_da_viagem

    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, token):
        self._token = token

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def viagem_id(self):
        return self._viagem_id
    
    @viagem_id.setter
    def viagem_id(self, viagem_id):
        self._viagem_id = viagem_id
    
    @property
    def letreiro(self):
        return self._letreiro
    
    @letreiro.setter
    def letreiro(self, letreiro):
        self._letreiro = letreiro

    @property
    def linha_nome(self):
        return self._linha_nome
    
    @linha_nome.setter
    def linha_nome(self, linha_nome):
        self._linha_nome = linha_nome
    
    @property
    def linha_numero(self):
        return self._linha_numero
    
    @linha_numero.setter
    def linha_numero(self, linha_numero):
        self._linha_numero = linha_numero

    @property
    def horario_partida(self):
        return self._horario_partida

    @horario_partida.setter
    def horario_partida(self, horario_partida):
        self.horario_partida = horario_partida

    @property
    def horario_chegada(self):
        return self._horario_chegada
        
    @horario_chegada.setter
    def horario_chegada(self, horario_chegada):
        self.horario_chegada = horario_chegada

    @property
    def origem(self):
        return self._origem.nome

    @origem.setter
    def origem(self, origem):
        self._origem = origem

    @property
    def destino(self):
        return self._destino.nome

    @destino.setter
    def destino(self, destino):
        self._destino = destino

    @property
    def passageiro(self):
        return self._passageiro.nome

    @passageiro.setter
    def passageiro(self, passageiro):
        self._passageiro = passageiro

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
