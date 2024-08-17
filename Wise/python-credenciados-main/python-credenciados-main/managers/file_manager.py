from datetime import datetime as dt
from extras.maps import TABLES_COLUMNS
from managers.teams_manager import send_card


def to_str(date: dt, format: str='%d/%m/%Y %H:%M:%S'):
    ''' Retorna a data no formato especificado '''

    if isinstance(date, dt):
        return date.strftime(format)
    
    else:
        return date


def validate_columns(table_info: list, table_name: str):
    ''' Valida se existe alguma coluna que não foi mapeada '''

    # Pegando todas as colunas da tabela
    all_columns = set()
    for register in table_info:
        for key in register.keys():
            all_columns.add(key)

    # Pegando todas as colunas mapeadas
    map_columns = TABLES_COLUMNS[table_name]
    map_columns = set(map_columns.keys())

    # Vendo a diferença entre elas
    not_map = all_columns - map_columns

    if not_map:     
        send_card({
            'TITLE': 'COLUNAS NÃO MAPEADA',
            'TITLE_SUBTITLE': f'Tabela: {table_name}',
            'MSG': f'Colunas não mapeadas: {", ".join(list(not_map))}'
        })
        return False

    else:
        return True
    

def get_temp_name(db_str: str, table_name: str):
    ''' Retorna o nome da tabela adicionando o prefixo TEMP_ e limitando o nome a 30 caracteres '''
    
    new_table_name = f'TEMP_{table_name}' # Adicionando prefixo TEMP_
    new_table_name = new_table_name[:30]  # Garantindo o tamanho maximo de 30 caracteres 

    if db_str:
        return f'{db_str}.{new_table_name}'    
    
    else:
        return new_table_name


def reorder_dict(original_dict: dict, order: list):
    ''' Altera a order das chaves de um dicionario com base no nome da tabela '''

    new_data = []
    for old_data in original_dict:
        new_data.append({key: old_data[key] for key in order})

    return new_data


def remove_keys(data: list, columns_to_remove: list):
    ''' Remove as chaves passadas por parametro '''

    new_data = []
    for old_data in data:
        new_data.append({key: old_data[key] for key in list(old_data.keys()) if key not in columns_to_remove})

    return new_data


def get_sum(data: list, key: str):
    ''' Retorna a soma de todos os valores de determinada chave '''

    return sum(log[key] for log in data)
