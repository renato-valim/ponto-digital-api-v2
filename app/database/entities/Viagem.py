from app.database.entities.Ponto import Ponto
from app.database.entities.Passageiro import Passageiro

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
            viagem_id = None):

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
            "viagem_id":self._viagem_id
        }
    
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
