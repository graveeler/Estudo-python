import time
from extras.maps import TABLES_NAME, TABLES_COLUMNS, REORDER_COLUMNS, CLOB_COLUMNS
from managers.config import config as c
from managers.log_manager import set_logfile, log_exception, logger_msg, add_log, get_time, get_date, get_date, sum_steps, all_times_report, get_steps_time, close_log
from managers.gogs_manager import get_gogs_files
from managers.file_manager import get_temp_name, reorder_dict, validate_columns, remove_keys
from managers.teams_manager import send_card
from managers.database_manager import get_tables_list, get_data, send_data, execute_statements, validate_table, drop_table, rename_table

CHUNK_SIZE = 1000
RETRY_COUNT = 1


def remove_temps(all_tables: str):
    ''' Remove todas as tabelas temporarias que acabaram remanescendo no banco de alguma execução de rotina antiga '''

    for table in all_tables:
        try:
            temp_table_name = get_temp_name(False, f'{c.s_prefix}{TABLES_NAME[table]}') 
            
            if validate_table(temp_table_name):
                if not drop_table(f'{c.o_auth}.{temp_table_name}'):
                    raise Exception()
        
        except Exception as e:
            log_exception(e, '| REMOVE TEMP | Removendo tabelas temporarias', {
                'TITLE': 'REMOVENDO TEMPS',
                'TITLE_SUBTITLE': 'Inicio da rotina',
                'MSG': f'Falha no drop das tabelas temporarias na tabela: {table}'}, exit=True) # Força o encerramento da rotina


def create_temp_table(table_name: str, table_query:str):
    ''' Faz a criação da tabela temporaria onde serão inseridos os dados em chunks '''

    # ---- QUEBRANDO os comandos ----
    sql_statements = table_query.split(';')
    sql_statements = [stmt.strip() for stmt in sql_statements if stmt.strip()]

    c_succeed = execute_statements(sql_statements, table_name)
    if not c_succeed:
        add_log(f'|===> Falha na criação da tabela: {table_name}', 'e')
        return False
    

    # ---- VALIDANDO temp ----   
    v_succeed = validate_table(table_name.replace(f'{c.o_auth}.', ''))
    if not v_succeed:
        add_log(f'|===> Falha na criação da tabela: {table_name}', 'e')
    
    return v_succeed


def generate_sql(table_name: str, data: list):
    ''' Gera a string sql e envia os dados para o banco Oracle '''

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


def update_clob(data: list, table_name: str):
    ''' Monta as queries para o update das tabelas que possuem colunas to tipo CLOB '''

    clob_columns = CLOB_COLUMNS[table_name]['column']
    data = reorder_dict(data, REORDER_COLUMNS[table_name])
    data_without_clob = remove_keys(data, clob_columns)    
    where_columns = CLOB_COLUMNS[table_name]['cd']


    # ---- Add CLOB VAZIOS ----
    empty_clob = {clob: None for clob in clob_columns} 
    validated_data_without_clob = []
    for old_data in data_without_clob:
        validated_data_without_clob.append({**old_data, **empty_clob})

    c_succeed = generate_sql(table_name, validated_data_without_clob) # Enviando os dados sem CLOB

    if not c_succeed:
        return False
    
    for clob_column in clob_columns:
        set_clause = f"{clob_column} = :1"
        where_clause = " AND ".join([f"{col} = :{i+2}" for i, col in enumerate(where_columns)])

        sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"


        # ---- REORDENANDO colunas ----
        transformed_data = [] # Reordenando as informações para a query
        for row in data:
            update_value = str(row[clob_column])
            where_values = [row[col] for col in where_columns]
            transformed_data.append((update_value, *where_values))


        # ---- ENVIANDO informações ----
        if not send_data(transformed_data, sql, table_name): # Se falhar o envio dos dados  
            add_log('>>>///>>> FALHA DE INSERT - Retrying...')
            time.sleep(10)
            
            if not send_data(transformed_data, sql, table_name):
                return False
            
    return True


def transfer_data(data: list, table_name: str):
    ''' Monta a query sql que insere os dados na tabela temporaria no Oracle e envia os dados '''

    if table_name in REORDER_COLUMNS: # Tabelas com CLOB        
        succeed = update_clob(data, table_name)

    else:
        succeed = generate_sql(table_name, data)
    
    return succeed


def replace_columns(dict_info: list, map: dict):
    ''' Substitui o nome das colunas conforme mapeamento '''

    return {map.get(k, k): v for k, v in dict_info.items()}


def run_routine():
    ''' Rotina que faz a extraçao das collection do Mongo e add em stage '''

    # ---- Ativando LOGS ---- 
    set_logfile('CREDENCIADOS')
    routine_start_time = logger_msg() 
    extraction_date = get_date()
    
    all_json_logs = []
    all_time_logs = []
    drop_map = []


#                       -----------------
# ===================> | EXTRACT SECTION | <===================
#                       -----------------
    # ---- Gogs ----
    try:
        add_log('|===> Extraindo do Gogs')
        tables_schemas = get_gogs_files()

        if not tables_schemas:
            raise Exception('| GOGS | Falha ao extrair schemas tabelas do Gogs')
    
    except Exception as e:
        log_exception(e, '| SCHEMAS | Extraindo schemas das tabelas', {
            'TITLE': 'EXTRAINDO SCHEMAS DE TABELAS',
            'TITLE_SUBTITLE': 'Inicio da Rotina',
            'MSG': 'Conexão com Gogs'}, exit=True) # Força o encerramento da rotina
    

    # ---- MySQL ----
    try:
        add_log('|===> Extraindo do MySQL')
        all_tables = get_tables_list()

        if not all_tables:
            raise Exception('| MYSQL | Falha ao extrair tabelas do MySQL')
    
    except Exception as e:
        log_exception(e, '| TABELAS | Extraindo tabelas', {
            'TITLE': 'EXTRAINDO TABELAS',
            'TITLE_SUBTITLE': 'Inicio da Rotina',
            'MSG': 'Conexão com MySQL'}, exit=True) # Força o encerramento da rotina
        

    # ---- Removendo TEMPORARIAS ----
    remove_temps(all_tables)
    
    for table in all_tables:
        try:
            e_start = add_log(f'|----> Iniciando tabela: {table}', return_time=True)


            # ---- Populando INFORMAÇÕES ----
            try:
                table_name = f'{c.o_auth}.{c.s_prefix}{TABLES_NAME[table]}'
                temp_table_name = get_temp_name(c.o_auth, f'{c.s_prefix}{TABLES_NAME[table]}')                
                
                json_log = {'NM_ROTINA': c.r_name, 'NM_TABELA': table_name, 'NM_ORIGEM': table, 'DH_INICIO_EXECUCAO': extraction_date}
            
            except Exception as e:
                log_exception(e, '| TABELA | Tabela não mapeada', {
                    'TITLE': 'TABELA NÃO MAPEADA',
                    'TITLE_SUBTITLE': f'Tabela: {table}',
                    'MSG': 'Tabela nova sem mapeamento'})
                continue


            # ---- Validando TABELA ----
            try:
                if table_name not in tables_schemas:
                    raise Exception()

            except Exception as e:
                log_exception(e, '| SCHEMA | Tabela sem schema', {
                    'TITLE': 'TABELA SEM SCHEMA',
                    'TITLE_SUBTITLE': f'Tabela: {table}',
                    'MSG': 'Tabela não possuí schema no Gogs'})
                continue


            # ---- Extraindo DADOS ---- 
            try:
                table_info = get_data(table)

                if isinstance(table_info, list) and table_info == []:
                    add_log(f'| MYSQL | Tabela vazia {table}')  
                    continue
                
                elif not table_info:
                    raise Exception(f'| MYSQL | Falha ao extrair tabela: {table}')                
           
            except Exception as e:
                remove_temps(all_tables) # Limpa os temps que foram executados com sucesso
                log_exception(e, '| TABELA | Extraindo tabela', {
                    'TITLE': 'EXTRAINDO TABELA',
                    'TITLE_SUBTITLE': f'Tabela: {table}',
                    'MSG': 'Trazendo registros do MySQL'}, exit=True) # Força o encerramento da rotina


            # ---- LOGS ----
            e_time = time.time() - e_start
            json_log['DS_TEMPO_EXTRACAO'] = get_time(e_time)
            json_log['QT_TEMPO_EXTRACAO_SEG'] = e_time
            json_log['QT_LINHAS_ORIGEM'] = len(table_info)
        
        except Exception as e:
            remove_temps(all_tables) # Limpa os temps que foram executados com sucesso
            log_exception(e, f'| EXTRAÇÃO | Erro na tabela: {table}', {
                'TITLE': 'EXTRAÇÃO',
                'TITLE_SUBTITLE': f'Tabela: {table}',
                'MSG': f'Erro durante a etapa de extracao para tabela: {table} com destino tabela {table_name}'}, exit=True) # Força o encerramento da rotina


#                       -------------------
# ===================> | TRANSFORM SECTION | <===================
#                       -------------------
         
        try:
            t_start = time.time()    

            # ---- VALIDANDO tabelas ----
            if not validate_columns(table_info, table):
                add_log(f'| TRANSFORMAÇÃO | COLUNAS NÃO MAPEADAS | Erro na validação das colunas da tabela: {table}', 'e')
                send_card({
                    'TITLE': 'COLUNAS SEM MAPEAMENTO',
                    'TITLE_SUBTITLE': f'Tabela: {table}',
                    'MSG': f'TABELA NÃO EXECUTADA! Novas colunas adicionadas na tabela que não estão mapeadas no ETL'
                }, error=True)
                continue


            # ---- Substituindo COLUNAS ---- 
            updated_table_info = [replace_columns(d, TABLES_COLUMNS[table]) for d in table_info]
            

            # ---- LOGS ----
            t_time = time.time() - t_start
            json_log['DS_TEMPO_TRANSFORMACAO'] = get_time(t_time)
            json_log['QT_TEMPO_TRANSFORMACAO_SEG'] = t_time
            json_log['QT_LINHAS_PYTHON'] = len(updated_table_info)

        except Exception as e:
            remove_temps(all_tables) # Limpa os temps que foram executados com sucesso
            log_exception(e, f'| TRANSFORMAÇÃO | Erro na tabela: {table}', {
                'TITLE': 'TRANSFORMAÇÃO',
                'TITLE_SUBTITLE': f'Tabela: {table}',
                'MSG': f'Erro durante a etapa de transformação para tabela: {table} com destino tabela {table_name}'}, exit=True) # Força o encerramento da rotina


#                       --------------
# ===================> | LOAD SECTION | <===================
#                       --------------
    
        l_start = add_log(f'|-> Total linhas: {len(updated_table_info)}', return_time=True)


        # ---- CRIANDO tabela temporaria ----
        try:
            if not create_temp_table(temp_table_name, tables_schemas[table_name]):
                continue # Vai para a proxima tabela
        
        except Exception as e:
            remove_temps(all_tables) # Limpa os temps que foram executados com sucesso
            log_exception(e, f'| LOAD | Criando temp: {temp_table_name}', {
                'TITLE': 'LOAD CRIANDO TEMP',
                'TITLE_SUBTITLE': f'Tabela: {table}',
                'MSG': f'Falha na criação da tabela temporaria: {temp_table_name}: da tabela: {table_name}'}, exit=True) # Força o encerramento da rotina


        # ---- INSERINDO dados ----
        for i in range(0, len(updated_table_info), CHUNK_SIZE):
            try:
                data = updated_table_info[i: i + CHUNK_SIZE]
                succeed = transfer_data(data, temp_table_name)
                
                if not succeed:
                    add_log(f'==> | INDEX | Index: {i} não adicionado')
                    raise Exception(f'Falha ao enviar o index: {i}')

            except Exception as e:
                remove_temps(all_tables) # Limpa os temps que foram executados com sucesso
                log_exception(e, f'| CARGA | Transferindo para: {table_name}', {
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


    # ---- DROP tabela original ----
    for succeed_load in drop_map:
        if drop_table(succeed_load['original']):

            # ---- RENAME tabela temporaria ----
            rename_table(succeed_load['temp'], succeed_load['original'])
        
        else:
            continue


    # ---- LOGS FINAIS ----
    total_time = time.time() - routine_start_time
    all_times_report(sum_steps(all_json_logs, total_time, all_time_logs))
    close_log(logger_msg(total_time), all_json_logs, extraction_date) 


if __name__ == '__main__':
    run_routine()    
