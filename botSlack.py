import requests
import json

def abrir_chamado(mediaCPU):
    # token do bot
    slack_token = 'xoxp-5817164342611-5814344897077-5881424142256-ce0b3bfe98c4cf50776956c49a25a1b1'
    # canal que o bot irá mandar as mensagens
    slack_channel = 'C05QQUXPKHN'

    # Configurações do bot com o python
    def post_message_to_slack(text, blocks = None):
        return requests.post('https://slack.com/api/chat.postMessage', {
            'token': slack_token,
            'channel': slack_channel,
            'text': text,
            'blocks': json.dumps(blocks) if blocks else None
        }).json()	

    # Escolhendo mensagem para ser enviada
    slack_info = f"""

        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥                                                                                                     
    A porcentagem de uso da sua máquina está ultrapassando o limite estipulado, está em {mediaCPU} %
    
    """
    
    post_message_to_slack(slack_info)
