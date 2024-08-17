import requests, json
from managers.config import config as c


def send_card(infos:dict, error:bool=False):
    ''' Monta e envia um card para o teams | Estrutura do infos    
        {
            'TITLE': Titulo do card (maior)
            'TITLE_SUBTITLE': Mensagem que vai no titulo do card (menor)
            'MSG': Mensagem personalizada que vai no corpo do card
            'LOG': Mensagem do log caso tenha dado erro
        }'''


    # -------- MONTANDO card --------
    card = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "1f84d4",
        "summary": 'Redes Sociais',
        "sections": [{
            "activityTitle": f'[E] {infos["TITLE"]}' if error else infos["TITLE"],
            "activitySubtitle": infos['TITLE_SUBTITLE'],
            "activityImage": 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1p1MfQUSClpYZVtul5_SnpkdTDbadOqZENYgUC4k6UMaJ729SF9j3npa7HrXm6SU9DQI&usqp=CAU',
            "facts": [
            {
                "name": "Mensagem",
                "value": infos['MSG']
            }],
            "markdown": True
        }]    
    }

    if 'LOG' in infos.keys():
        card['sections'][0]['facts'].append({"name": "Log","value": infos['LOG']})


    # -------- ENVIANDO card --------
    payload_json = json.dumps(card)
    requests.post(c.teams, data=payload_json, headers={"Content-Type": "application/json"})
