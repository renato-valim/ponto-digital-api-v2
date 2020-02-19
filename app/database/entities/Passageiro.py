import json


class Passageiro:
    def __init__(self):
        self._id = None
        self._nome_usuario = None
        self._nome = None
        self._cpf = None
        self._rg = None
        self._data_nascimento = None
        self._genero = None
        self._tipo = None
        self._endereco = None
        self._senha = None

    @property
    def nome(self):
        return self._nome

    def toDict(self):
        return {
            "nome": self._nome,
            "nome_usuario": self._nome_usuario,
            "tipo": self._tipo,
            "endereco": self._endereco,
            "rg": self._rg,
            "cpf": self._cpf,
            "id": self._id,
            "data_nascimento": self._data_nascimento,
            "genero": self._genero
        }

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome_usuario(self):
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario):
        self._nome_usuario = nome_usuario

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
