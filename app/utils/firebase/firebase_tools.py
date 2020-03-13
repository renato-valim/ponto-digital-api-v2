from firebase_admin import messaging
from firebase_admin import credentials


def enviar_notificacao(title, body, token): 
    try:
        notification = messaging.Notification(
            title=title, body=body)

        message = messaging.Message(
            notification=notification,
            token=token
        )

        response = messaging.send(message)

        print('Successfully sent message:', response)
    except Exception as e:
        print('Error sending message: {}'.format(e))

def lembrete_usuario(viagem):
    try:
        notificacao = {
            'title':'',
            'body':''
        }

        if(viagem._fase_da_viagem == "Embarque" and viagem._minutos_restantes != 0):
            notificacao['title'] = 'Seu ônibus chegará em {} minutos'.format(str(viagem._minutos_restantes))
            notificacao['body'] = 'Fique atento às notificações'

        elif(viagem._fase_da_viagem == "Desembarque" and viagem._minutos_restantes != 0):
            notificacao['title'] = 'Você chegará ao seu destino em {} minutos'.format(str(viagem._minutos_restantes))
            notificacao['body'] = 'Fique atento às notificações'
        
        elif(viagem._fase_da_viagem == "Embarque" and viagem._minutos_restantes == 0):
            notificacao['title'] = 'Seu ônibus está prestes a chegar'
            notificacao['body'] = 'Prepare-se para o embarque'

        elif(viagem._fase_da_viagem == "Desembarque" and viagem._minutos_restantes == 0):
            notificacao['title'] = 'Você está prestes a chegar ao seu destino'
            notificacao['body'] = 'Prepare-se para o desembarque'
        
        enviar_notificacao(
            title=notificacao['title'],
            body=notificacao['body'],
            token=viagem._token
        )
    except Exception as e:
        print('Error sending message: {}'.format(e))