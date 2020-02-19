import requests


def planejar_viagem(origem, destino):
    """
    Consome API Directions e planeja uma viagem a partir dos pontos de origem e destino

    - **parametros**::
        - origin (str): Ponto de Origem da viagem
        - destiny (str): Ponto de Destino da viagem
    """

    payload = {
        'origin': origem,
        'destination': destino,
        'mode': "transit",
        'key': 'AIzaSyCprQD8WAAsH4fQDgH_zRGR_oqHMvhWDp4'
    }
    try:
        return requests.get(
            'https://maps.googleapis.com/maps/api/directions/json', params=payload).json()
    except:
        raise Exception("Falha na requisição")


def geocodificar_coordenadas(lat, lng):
    """
    Consome API Geocoding e retorna um endereço baseado nas suas coordenadas geográficas

    - **parametros**::
        - lat (int): Latitude do endereço
        - lng (int): Longitude do endereço
    """

    payload = {
        'latlng': '{0},{1}'.format(lat, lng),
        'key': 'AIzaSyCprQD8WAAsH4fQDgH_zRGR_oqHMvhWDp4'
    }
    try:
        return requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json", params=payload).json()
    except:
        raise Exception("Falha na requisição")


def geocodificar_endereco(endereco):
    """
    Consome API Geocoding e retorna um endereço baseado no seu nome

    - **parametros**::
        - address (str): Nome do endereço
    """

    payload = {
        'address': endereco,
        'key': 'AIzaSyCprQD8WAAsH4fQDgH_zRGR_oqHMvhWDp4'
    }
    try:
        return requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json', params=payload).json()
    except:
        raise Exception("Falha na requisição")


def proximas_partidas(id):
    try:
        return requests.get(
            'https://editor.mobilibus.com/web/get-proximas-partidas/2563h/{0}'.format(id)).json()
    except:
        raise Exception("Falha na requisição")
