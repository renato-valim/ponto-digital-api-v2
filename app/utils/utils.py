import unicodedata
import re
import json
import firebase_admin
import datetime
from pytz import timezone
from firebase_admin import messaging
from firebase_admin import credentials

# FORMATA UMA STRING, TIRANDO SEUS ACENTOS E ESPAÇOS
def format_string(palavra):
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join(
        [c for c in nfkd if not unicodedata.combining(c)])

    return re.sub(
        '[^a-zA-Z0-9 \\\]', '', palavraSemAcento).replace(" ", "+")

def format_string_acentos(palavra):
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join(
        [c for c in nfkd if not unicodedata.combining(c)])

    return re.sub(
        '[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def to_esp(palavra):
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join(
        [c for c in nfkd if not unicodedata.combining(c)])
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    sem_acento = re.sub(
        '[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

    palavra_formatada = ""

    for letter in sem_acento:
        if letter in numeros and not ',' in palavra_formatada:
            indx = sem_acento.index(letter) - 1
            palavra_formatada = sem_acento[:indx] + \
                ', ' + sem_acento[indx + 1:]
            return palavra_formatada

# LE UM ARQUIVO JSON
def read_json_file(path):
    try:
        with open(path, encoding='utf-8') as fh:
            data = json.load(fh)

        fh.close()

        return data
    except json.JSONDecodeError:
        print("JSON DECODE ERROR")

def write_json_file(path, data):
    with open(path, 'w') as json_file:
        json.dump(data, json_file)

    json_file.close()

# DEVOLVE O HORARIO ATUAL NO FUSO HORARIO DE SAO PAULO

def current_date():
    # TIMECONFIG ==========================================
    data_atual = datetime.datetime.now()
    fuso_horario = timezone("America/Sao_Paulo")
    formatted_date = data_atual.astimezone(fuso_horario)
    current_date = formatted_date.strftime(
        '%Y-%m-%d %H:%M:%S')
    # =======================================================
    return current_date
