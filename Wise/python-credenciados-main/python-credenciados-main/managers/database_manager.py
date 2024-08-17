from sqlalchemy import Table, MetaData, select, inspect
from managers.log_manager import log_exception
from managers.integration_manager import open_mysql_conn, open_oracle_conn


def get_data(table_name: str):
    ''' Retorna dados de uma tabela do MySQL '''
    
    try:
        with open_mysql_conn() as db:       
            metadata = MetaData()
            table = Table(table_name, metadata, autoload_with=db)
            
            query = select(table)            
            result = db.execute(query)

            column_names = result.keys()
            data = []
            for row in result:
                data.append(dict(zip(column_names, row)))

            return data
    
    except Exception as e:
        log_exception(e, f'| GET | Obtendo dados da tabela: {table_name}')
        return False
    

def get_tables_list():
    ''' Retorna a lista de todas as tabelas do MySQL '''
    
    try:
        with open_mysql_conn() as db:
            inspector = inspect(db)
            return inspector.get_table_names()
    
    except Exception as e:
        log_exception(e, '| GET | Obtendo listagem das tabelas')
        return False
    

def send_data(data: list, sql: str, table_name: str):
    ''' Envia os dados para uma tabela no Oracle '''

    try:
        with open_oracle_conn() as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            conn.commit()
            
        return True
            
    except Exception as e:
        log_exception(e, f"| ENVIA DADOS | Transferindo dados para a tabela: {table_name}")
        return False
    

def execute_statements(statements: list, table_name: str):
    ''' Executa varias queries no banco de Stage do BI '''

    try:
        with open_oracle_conn() as conn:
            cursor = conn.cursor()
            
            for statement in statements:
                cursor.execute(statement)
            
            conn.commit()
            
            return True
            
    except Exception as e:
        log_exception(e, f"| EXECUTA QUERY | Executando queries em Stage para criação da tabela: {table_name}")
        return False
    

def validate_table(table_name: str):
    ''' Valida se uma tabela existe no banco de Stage do BI. Utilizando o user_tables ele ja busca por todas as tabelas do usuario na conexão, não havendo necessidade de enviar o mesmo concatenado no nome da tabela '''

    try:
        with open_oracle_conn() as conn:
            cursor = conn.cursor()        
            query = 'SELECT COUNT(*) FROM user_tables WHERE table_name = :table_name'
            cursor.execute(query, {"table_name": table_name})

            return cursor.fetchone()[0] > 0
            
    except Exception as e:
        log_exception(e, f"| TABELA EXISTE | Verificando se tabela: {table_name} existe no banco")
        return False
    

def drop_table(table_name: str):
    ''' Remove uma table do banco de Stage do BI '''

    try:
        with open_oracle_conn() as conn:
            cursor = conn.cursor()  
            query = f'DROP TABLE {table_name} PURGE'          
            cursor.execute(query)
            conn.commit()

            return True
            
    except Exception as e:
        log_exception(e, f"| DROP | Deletando tabela: {table_name}")
        return False
    

def rename_table(temp_table_name: str, table_name: str):
    ''' Altera o nome da tabela temporaria pelo nome da tabela original '''

    try:
        query = f"ALTER TABLE {temp_table_name} RENAME TO {table_name.replace('BI_STG.','')}" 
        
        with open_oracle_conn() as conn:
            cursor = conn.cursor()        
            cursor.execute(query)
            conn.commit()

            return True
            
    except Exception as e:
        log_exception(e, f"| RENAME | Renomeando tabela: {table_name}")
        return False
