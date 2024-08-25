import time, json, requests
from extras.maps import COLUMNS, REORDER_COLUMNS, BACKUP_SCHEMA
from managers.config import config as c
from managers.log_manager import set_logfile, log_exception, logger_msg, add_log, get_time, get_date, get_date, sum_steps, all_times_report, get_steps_time, close_log
from managers.gogs_manager import get_gogs_files
from managers.file_manager import get_temp_name, validate_columns, reorder_dict
from managers.database_manager import send_data, execute_statements, validate_table, drop_table, rename_table

CHUNK_SIZE = 1000
RETRY_COUNT = 1
TABLE_NAME = 'SALES_FORCE'
URL_MAP = {
    'SALES_FORCE': c.a_sales,
    'SALES_FORCE_FACE': c.a_face,
    'SALES_FORCE_FACE_V2': c.a_face2}



def transfer_data(data: list, table_name: str):
    ''' Monta a query sql que insere os dados na tabela temporaria no Oracle e envia os dados '''

    columns = list(data[0].keys())
    columns_enum = [':' + str(i+1) for i in range(len(columns))]

    sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(columns_enum)})'
    
    transformed_data = [tuple(row[col] for col in columns) for row in data]

    succeed = send_data(transformed_data, sql, table_name)

    if not succeed: # Se falhar o envio dos dados
        add_log('>>>///>>> FALHA DE INSERT - Retrying...')
        time.sleep(10)
        
        return send_data(transformed_data, sql, table_name)
    
    return succeed


def create_temp_table(table_name: str, table_query:str):
    ''' Faz a criação da tabela temporaria onde serão inseridos os dados em chunks '''

    # ---- QUEBRANDO os comandos ----
    sql_statements = table_query.split(';')
    sql_statements = [stmt.strip() for stmt in sql_statements if stmt.strip()]

    c_succeed = execute_statements(sql_statements, table_name)
    if not c_succeed:
        add_log(f'|=-=> Falha na criação da tabela: {table_name}', 'e')
        return False
    

    # ---- VALIDANDO temp ----   
    v_succeed = validate_table(table_name.replace(f'{c.o_auth}.', ''))
    if not v_succeed:
        add_log(f'|=-=> Falha na criação da tabela: {table_name}', 'e')
    
    return v_succeed


def replace_columns(dict_info: list, map: dict):
    ''' Substitui o nome das colunas conforme mapeamento '''

    return {map.get(k, k): v for k, v in dict_info.items()}


def remove_temps():
    ''' Remove todas as tabelas temporarias que acabaram remanescendo no banco de alguma execução de rotina antiga '''

    add_log('|--> Removendo temporárias')
    for table in c.s_tables:
        try:
            temp_table_name = get_temp_name(False, f'{c.s_prefix}{table}') 
            
            if validate_table(temp_table_name):
                if not drop_table(f'{c.o_auth}.{temp_table_name}'):
                    raise Exception()
        
        except Exception as e:
            log_exception(e, '| REMOVE TEMP | Removendo tabelas temporarias', {
                'TITLE': 'REMOVENDO TEMPS',
                'TITLE_SUBTITLE': 'Inicio da rotina',
                'MSG': f'Falha no drop das tabelas temporarias na tabela: {table}'}, exit=True) # Força o encerramento da rotina


def get_token():
    ''' Retorna o Token para executar as requisições na API '''

    try:
        add_log('|--> Extraindo Token')
        url = f'{c.a_purl}auth.{c.a_murl}/v2/token'
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({
            "grant_type": c.a_grant,
            "client_id": c.a_id,
            "client_secret": c.a_secret})
        
        try:
            resp = requests.post(url, headers=headers, data=payload)
            resp.raise_for_status()
        
        except:
            raise Exception()

        resp = resp.json()
        return {'Authorization': f'Bearer {resp["access_token"]}'}
    
    except Exception as e:
        log_exception(e, '| TOKEN | Extraindo token', {
            'TITLE': 'EXTRAINDO TOKEN',
            'TITLE_SUBTITLE': 'Falha na extração',
            'MSG': 'Falha na extração do Token'}, exit=True) # Força o encerramento da rotina


def run_routine():
    ''' Rotina que faz a extraçao da informação da API e adiciona em stage '''

    # ---- Ativando LOGS ---- 
    set_logfile(c.s_table)
    routine_start_time = logger_msg() 
    extraction_date = get_date(date_form=True)


#                       -----------------
# ===================> | EXTRACT SECTION | <===================
#                       -----------------

    e_start = time.time()
    all_json_logs = []
    all_time_logs = []
    drop_map = []        


    # ---- Token ----
    token = get_token()


    # ---- Gogs ----
    try:
        add_log('|--> Extraindo do Gogs')
        table_schemas = get_gogs_files()

        if not table_schemas:
            raise Exception('| GOGS | Falha ao extrair schemas tabelas do Gogs')
    
    except Exception as e:
        log_exception(e, '| SCHEMAS | Extraindo schemas das tabelas', {
            'TITLE': 'EXTRAINDO SCHEMAS DE TABELAS',
            'TITLE_SUBTITLE': 'Inicio da Rotina',
            'MSG': 'Conexão com Gogs'}, exit=True) # Força o encerramento da rotina
                

    # ---- Removendo TEMPORARIAS ----
    remove_temps()

    for table in c.s_tables:
        try:
            e_start = add_log(f'|----> Iniciando tabela: {table}', return_time=True)


            # ---- Populando INFORMAÇÕES ----
            all_data = []  
            url = URL_MAP[table]
            table_name = f'{c.o_auth}.{c.s_prefix}{table}'
            temp_table_name = get_temp_name(c.o_auth, f'{c.s_prefix}{table}')        
            json_log = {'NM_ROTINA': c.r_name, 'NM_TABELA': table_name, 'NM_ORIGEM': 'API CALL', 'DH_INICIO_EXECUCAO': extraction_date}
            
            add_log('|--> Chamando API')
            while url:

                # ---- Chamando API ----
                try:
                    resp = requests.get(url, headers=token)
                    resp.raise_for_status()
                
                except:
                    raise Exception()
                    

                # ---- EXTRAINDO dados ----
                data = resp.json()
                data_len = data.get('count', 0)
                for item in data.get('items', []):
                    all_data.append(item.get('values'))
                

                # ---- Buscando PAGINAÇÃO ----
                next_url = data.get('links', {}).get('next')
                
                if not next_url:
                    break
                
                url = f'{c.a_purl}rest.{c.a_murl}/data{next_url}'


            # ---- LOGS ----
            e_time = time.time() - e_start
            json_log['DS_TEMPO_EXTRACAO'] = get_time(e_time)
            json_log['QT_TEMPO_EXTRACAO_SEG'] = e_time
            json_log['QT_LINHAS_ORIGEM'] = data_len

        except Exception as e:
            remove_temps() # Limpa os temps que foram executados com sucesso
            log_exception(e, '| EXTRAÇÃO | Realizando requests', {
                'TITLE': 'EXTRAÇÃO',
                'TITLE_SUBTITLE': f'Tabela: {table}',
                'MSG': f'Falha nas chamadas a API para popular a tabela: {table}'}, exit=True) # Força o encerramento da rotina


#                       -------------------
# ===================> | TRANSFORM SECTION | <===================
#                       -------------------
         
        try:
            t_start = time.time()    
            add_log('|--> Iniciando Transformação')


            # ---- VALIDANDO tabelas ----
            if not validate_columns(all_data, table):
                add_log(f'| TRANSFORMAÇÃO | COLUNAS NÃO MAPEADAS | Erro na validação das colunas da tabela', 'e')
                raise Exception('Colunas SEM MAPEAMENTO')


            # ---- Substituindo COLUNAS ---- 
            updated_table_info = [replace_columns(d, COLUMNS[table]) for d in all_data]
            if table in REORDER_COLUMNS:
                updated_table_info = reorder_dict(updated_table_info, REORDER_COLUMNS[table])


            # ---- LOGS ----
            t_time = time.time() - t_start
            json_log['DS_TEMPO_TRANSFORMACAO'] = get_time(t_time)
            json_log['QT_TEMPO_TRANSFORMACAO_SEG'] = t_time
            json_log['QT_LINHAS_PYTHON'] = len(updated_table_info)

        except Exception as e:
            remove_temps() # Limpa os temps que foram executados com sucesso
            log_exception(e, f'| TRANSFORMAÇÃO | Erro na tabela', {
                'TITLE': 'TRANSFORMAÇÃO',
                'TITLE_SUBTITLE': f'Tabela: {table}',
                'MSG': f'Erro durante a etapa de transformação para tabela: {table}'}, exit=True) # Força o encerramento da rotina


#                       --------------
# ===================> | LOAD SECTION | <===================
#                       --------------
    
        l_start = add_log('|===> Iniciando Load', return_time=True)    


        # ---- CRIANDO tabela temporaria ----
        try:
            add_log('|--> Criando temporária')
            if table not in BACKUP_SCHEMA:
                if not create_temp_table(temp_table_name, table_schemas[table_name]):
                    raise Exception()
                
            else:
                if not create_temp_table(temp_table_name, BACKUP_SCHEMA[table]):
                    raise Exception()
        
        except Exception as e:            
            log_exception(e, f'| LOAD | Criando temp: {temp_table_name}', {
                'TITLE': 'LOAD CRIANDO TEMP',
                'TITLE_SUBTITLE': f'Tabela: {table}',
                'MSG': f'Falha na criação da tabela temporaria: {temp_table_name}'}, exit=True) # Força o encerramento da rotina


        # ---- INSERINDO dados ----
        add_log('|--> Iniciando envios')
        for i in range(0, len(updated_table_info), CHUNK_SIZE):
            try:
                data = updated_table_info[i: i + CHUNK_SIZE]
                succeed = transfer_data(data, temp_table_name)
                
                if not succeed:
                    add_log(f'=-=> | INDEX | Index: {i} não adicionado')
                    raise Exception(f'Falha ao enviar o index: {i}')

            except Exception as e:
                remove_temps() # Remove a tabela criada
                log_exception(e, f'| CARGA | Transferindo para STG', {
                    'TITLE': f"ERRO DE CARGA",
                    'TITLE_SUBTITLE': f'Tabela: {table_name}',
                    'MSG': f"Falha no index: {i}. Tabela não atualizada!"}, exit=True) # Força o encerramento da rotina
                
        
        # ---- CRIANDO map de sucesso ----
        drop_map.append({'original': table_name, 'temp': temp_table_name}) 
        

        # ---- LOGS ----
        l_time = time.time() - l_start
        json_log['DS_TEMPO_LOAD'] = get_time(l_time)
        json_log['QT_TEMPO_LOAD_SEG'] = t_time

        all_json_logs.append(json_log)
        all_time_logs.append(get_steps_time(table_name, e_start, e_time, t_time, l_time))

    for succeed_load in drop_map:    
        
        # ---- DROP tabela original ----     
        if validate_table(succeed_load['original'].replace(f'{c.o_auth}.', '')):
            add_log('|--> Dropando original')   
            drop_table(succeed_load['original'])

        # ---- RENAME tabela temporaria ----
        add_log('|--> Renomeando temporária')
        rename_table(succeed_load['temp'], succeed_load['original'])


    # ---- LOGS FINAIS ----
    total_time = time.time() - routine_start_time
    logger_msg(total_time)
    all_times_report(sum_steps(all_json_logs, total_time, all_time_logs))
    close_log(total_time, all_json_logs, extraction_date)


if __name__ == '__main__':
    run_routine()    
