import cx_Oracle
from contextlib import contextmanager
from managers.config import config as c
from managers.teams_manager import send_card


@contextmanager
def open_oracle_conn():
    ''' Abre uma conexão com o Oracle e retorna o cursor '''
    
    try:
        conn = cx_Oracle.connect(c.o_str)
        yield conn
            
    except:
        send_card({
            'TITLE': 'ABRINDO CONEXAO COM ORACLE',
            'TITLE_SUBTITLE': 'Erro abrir uma conexão com o Oracle',
            'MSG': f'Erro no context manager durante a criaçao da conexão com o banco de dados Oracle'}, error=True)
        
    finally:
       conn.close()
