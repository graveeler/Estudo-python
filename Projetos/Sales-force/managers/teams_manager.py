import requests, json
from managers.config import config as c


def send_card(infos:dict, error:bool=False, final: dict=False):
    ''' Monta e envia um card para o teams | Estrutura do infos    
        {
            'TITLE': Titulo do card (maior)
            'TITLE_SUBTITLE': Mensagem que vai no titulo do card (menor)
            'MSG': Mensagem personalizada que vai no corpo do card
            'LOG': Mensagem do log caso tenha dado erro
        }
        '''


    # -------- MONTANDO card --------
    card = {
        "title": f'[E] {infos["TITLE"]}' if error else infos["TITLE"],
        "subtitle": infos['TITLE_SUBTITLE'],
        "image": 'https://d3v6byorcue2se.cloudfront.net/contents/ffYmfEvYwJIyl3KkRlgv-350x350.png',
        "message": infos['MSG'],
        "log": None if not 'LOG' in infos.keys() else infos['LOG'],
        "final": isinstance(final, dict),
        "ext": None if not final else final['ext'], 
        "tra": None if not final else final['tra'], 
        "loa": None if not final else final['loa'], 
        "err": None if not final else final['err'],
        "tot": None if not final else final['tot'],
        "tab": None if not final else final['tab']
    }

    # -------- ENVIANDO card --------
    payload_json = json.dumps(card)
    requests.post(c.teams, data=payload_json, headers={"Content-Type": "application/json"})

