from app.api.core_api import planejar_viagem

from app.database.entities.Ponto import Ponto
from app.database.entities.Viagem import Viagem
from app.database.daos.PassageiroDAO import PassageiroDAO

from app.utils.utils import read_json_file, write_json_file

from app.api.core_api import proximas_partidas

from app.database.daos.PontoDAO import PontoDAO

def viagem_completa(origem, destino, passageiro):
    informacoes_viagem = planejar_viagem(origem, destino)
    
    pontos_indaiatuba_dir = 'app/database/archives/pontos_indaiatuba.json'

    pontos_indaiatuba = read_json_file(pontos_indaiatuba_dir)

    viagens = []

    for step in informacoes_viagem['routes'][0]['legs'][0]['steps']:
        if 'transit_details' in step:
            viagem = Viagem()
            viagem._passageiro = passageiro

            viagem._horario_partida = step['transit_details']['departure_time']['text']
            viagem._horario_chegada = step['transit_details']['arrival_time']['text']
            viagem._letreiro = step['transit_details']['headsign']
            viagem._linha_numero = step['transit_details']['line']['short_name']

            for ponto in pontos_indaiatuba:
                if(ponto['nome'] == step['transit_details']['departure_stop']['name']):
                    viagem._origem = PontoDAO.select(ponto['id'])
                elif(ponto['nome'] == step['transit_details']['arrival_stop']['name']):
                    viagem._destino = PontoDAO.select(ponto['id'])
            
            viagem_proximas_partidas = proximas_partidas(viagem._origem.cod)

            for partida in viagem_proximas_partidas['partidas']:
                if(partida['routeShortName'] == viagem._linha_numero and partida['tripHeadsign'] == viagem._letreiro):
                    viagem._linha_nome = partida['routeLongName']
                    viagem._viagem_id = partida['tripId']
            
            viagens.append(viagem.toDict())

    return viagens

def atualizar_veiculo_viagem(id, veiculo):
    passageiros_file = 'app/database/temp/passageiros.json'
    passageiros = read_json_file(passageiros_file)

    passageiros[str(id)]['veiculo'] = veiculo

    write_json_file(passageiros_file, passageiros)

def finalizar_viagem(id):
    passageiros_file = 'app/database/temp/passageiros.json'
    passageiros = read_json_file(passageiros_file)

    del passageiros[str(id)]

    write_json_file(passageiros_file, passageiros)


def registrar_viagem(viagem):
    try:
        viagem_info = "app/database/temp/viagem/viagem_{}/info.json".format(viagem._id)

        write_json_file(viagem_info, viagem.toDict())

        passageiros_file = 'app/database/temp/passageiros.json'
        passageiros = read_json_file(passageiros_file)

        passageiros[str(viagem._id)] = {
            "nome_passageiro": viagem._passageiro.nome,
            "ponto_origem":viagem._origem.nome,
            "ponto_destino":viagem._destino.nome,
            "veiculo":viagem._veiculo
        }
                                                                        
        write_json_file(passageiros_file, passageiros)
    except Exception as e:
        print(e)
    