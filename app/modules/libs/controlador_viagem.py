import sys
import threading
import time
import datetime
import os

from app.api.core_api import proximas_partidas

from app.modules.libs.viagem_lib import registrar_viagem, atualizar_veiculo_viagem, finalizar_viagem
from app.utils.firebase.firebase_tools import lembrete_usuario, enviar_notificacao

from app.utils.utils import read_json_file

from app.database.entities.Viagem import Viagem

class ControladorViagem(threading.Thread):
    def __init__(self, viagem):
        threading.Thread.__init__(self)

        self.stopEvent = threading.Event()

        self.viagem = viagem
        self.viagem._fase_da_viagem = "Embarque"
        self.viagem._status = "EM ANDAMENTO"

        os.mkdir('app/database/temp/viagem/viagem_{}'.format(self.viagem._id))
        registrar_viagem(self.viagem)

        self.rotina_de_notificacoes = {
            '25': False,
            '20': False, 
            '15': False,
            '10': False,
            '5': False,
            '2': False,
            '0': False
        }

    def __setInterval(self):
        nextTime = time.time() + 1
        while not self.stopEvent.wait(nextTime - time.time()):
            nextTime += 1
            self.verificar_status_viagem()
            self.atualizar_status_viagem()
            self.salvar_alteracoes()
    
    def salvar_alteracoes(self):
        json_viagem = read_json_file('app/database/temp/viagem/viagem_{}/info.json'.format(self.viagem._id))

        self.viagem = Viagem.toObj(json_viagem)
    
    def verificar_status_viagem(self):

        try:
            status_dir = 'app/database/temp/viagem/viagem_{}/STATUS.txt'.format(self.viagem._id)
            status = open(status_dir, 'r')

            self.viagem._status = status.read()
            status.close()

            print(self.viagem._status)

            if(self.viagem._status == "CANCELADA" or self.viagem._status == "FINALIZADA"):
                self.cancel()
            
        except FileNotFoundError:
             print("Status externo não definido")
            
        

    def atualizar_tempo_restante(self):
        try:
            ponto = self.viagem._origem.cod if self.viagem._fase_da_viagem == "Embarque" else self.viagem._destino.cod
            for trip in proximas_partidas(ponto)['partidas']:
                if (trip['tripHeadsign'] == self.viagem._letreiro and trip['tripId'] == self.viagem._viagem_id):
                    self.viagem._controle_falha = 0
                    if(self.viagem._minutos_restantes != trip['minutosPartida']):
                        print("Minutos: {}".format(trip['minutosPartida']))
                        self.viagem._minutos_restantes = trip['minutosPartida']

                    if(trip['veiculo'] != 'None' and trip['veiculo'] != None and trip['veiculo'] != self.viagem._veiculo):
                        print("Veiculo: {}".format(trip['veiculo']))
                        self.viagem._veiculo = trip['veiculo']
                        atualizar_veiculo_viagem(self.viagem._id, self.viagem._veiculo)

                    registrar_viagem(self.viagem)
                    return 
            self.viagem._controle_falha += 1

        except Exception:
            pass
    
    def atualizar_status_viagem(self):
        self.atualizar_tempo_restante()

        if(self.viagem._controle_falha >= 30):
            self.cancel()
            self.viagem._status = "CANCELADA"
            registrar_viagem(self.viagem)
        
        if(str(self.viagem._minutos_restantes) in self.rotina_de_notificacoes and not self.rotina_de_notificacoes[str(self.viagem._minutos_restantes)]):
            lembrete_usuario(self.viagem)
            print("Notificação")
            self.rotina_de_notificacoes[str(self.viagem._minutos_restantes)] = True

        if(self.viagem._fase_da_viagem == "Desembarque" and self.viagem._minutos_restantes == 0):
            self.cancel()
            self.viagem._status = "FINALIZADA"
            registrar_viagem(self.viagem)
        
        elif(self.viagem._fase_da_viagem == "Embarque"  and self.viagem._minutos_restantes == 0):
            self.viagem._fase_da_viagem = "Desembarque"
            self.rotina_de_notificacoes = {
            '25': False,
            '20': False, 
            '15': False,
            '10': False,
            '5': False,
            '2': False,
            '0': False
            }
            registrar_viagem(self.viagem)
          
    def cancel(self):
        print("FIM DA VIAGEM")
        finalizar_viagem(self.viagem._id)
        self.stopEvent.set()
    
    def run(self):
        thread = threading.Thread(target=self.__setInterval)
        try:
            enviar_notificacao(
                title="Sua viagem foi inicializada",
                body="Fique atento às notificações",
                token=self.viagem._token
            )
            thread.start()
            #thread.join()
        except (KeyboardInterrupt, SystemExit):
            self.cancel()
            sys.exit()