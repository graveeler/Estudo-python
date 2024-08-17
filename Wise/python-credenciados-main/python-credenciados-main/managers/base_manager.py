import base64


def base(s: str):
    ''' Integrador de configuração '''
    
    try:
        return base64.b64decode(s.encode('utf-8')).decode('utf-8')
    
    except:
        return False
