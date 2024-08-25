import sys, traceback, inspect, time, logging, logzero, os, pytz
from logzero import logger, logfile
from datetime import datetime as dt
from managers.config import config as c
from managers.file_manager import to_str, get_sum
from managers.teams_manager import send_card
from managers.integration_manager import open_oracle_conn

ERROR_LIST = []


class CustomFormatter(logging.Formatter):
    ''' Classe que formata como as mensagens de log  vão ser inseridas no sistema '''
    
    def format(self, record):
        ''' Formata o atributo levelname da mensagem de log trazendo apenas a primeira letra'''
        
        record.levelname = record.levelname[0] # Transforma o levelname em uma letraarquivo
        
        return super().format(record)


def set_logfile(log_file: str):
    ''' Determina o logfile para a execução do script '''
    
    formatter = CustomFormatter('[%(levelname)s] %(message)s')
    logzero.formatter(formatter)
    
    logfile(f'logs/{log_file}.logs')


def log_exception(e: Exception, msg: str, card: dict=None, exit: bool=False):
    ''' Função que loga exceções no arquivo de log '''
        
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    filename = os.path.splitext(os.path.basename(frame.f_code.co_filename))[0]
    detailed_exp = traceback.format_exc()
    _,_, exc_tb = sys.exc_info()
    str_error_date, dt_error_date = get_date(both=True)
    error_line = exc_tb.tb_lineno
        
    full_msg = f"{str_error_date} {filename}: {msg}\n|====> Função: {func_name}() | Linha: {error_line} | Exception: {e}\n\n{detailed_exp}"
    add_log(full_msg, type='e', add_date=False)
    save_error(dt_error_date, filename, func_name, error_line, e, detailed_exp, msg)

    if card:
        card['LOG'] = msg
        send_card(card)

    if exit:
        add_log('| EXIT | Forçando EXIT da aplicação\n', type='w')
        call_procedure(error_log=f'Quantidade de errors: {len(ERROR_LIST)}')  
        sys.exit(1)

    return


def save_error(dt_error_date, filename, func_name, line, exec, detailed_exp, e_msg):
    ''' Salva o log de erro na tabela do Oracle '''
    
    error_log = {
        'NM_ROTINA': c.r_name,
        'DH_ERRO': dt_error_date,
        'NM_ARQUIVO': filename,
        'NM_FUNCAO': func_name,
        'NM_LINHA': line,
        'DS_MENSAGEM': e_msg,
        'DS_EXCECAO': exec,
        'DS_EXCECAO_DETALHADO': detailed_exp
    }

    columns = list(error_log.keys())
    columns_enum = [':' + str(i+1) for i in range(len(columns))]
    sql = f'INSERT INTO {c.o_log} ({", ".join(columns)}) VALUES ({", ".join(columns_enum)})'

    data = [tuple(error_log[col] for col in columns)]

    with open_oracle_conn() as conn:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()


def get_date(date_form: bool=False, both: bool=False):
    ''' Função que retorna a data e hora atual no fuso horário de São Paulo no formato dd/mm/yyyy hh:mm'''

    date = dt.now(pytz.timezone('America/Sao_Paulo'))
    
    if not date_form:
        return to_str(date)
    
    if both:
        return to_str(date), date
    
    return date


def add_log(msg: str, type: str='i', return_time: bool=False, add_date: bool=True):
    ''' Adiciona log no arquivo de log '''
    
    global ERROR_LIST

    if add_date:
        msg = f"{get_date()} {msg}"

    if type == 'i':
        logger.info(msg)

    elif type == 'e':
        logger.error(msg)
        ERROR_LIST.append(msg)

    elif type == 'w':
        logger.warning(msg)

    if return_time:
        return time.time()


def get_time(total_time: float):
    ''' Devolve o tempo de execução em horas, minutos e segundos '''        
    
    hours, rem = divmod(total_time, 3600)
    minutes, seconds = divmod(rem, 60)
    msg = f"{int(hours):0>2}:{int(minutes):0>2}:{int(seconds):0>2}"

    return msg


def logger_msg(time_start: float=0):
    ''' Salva a mensagem inicial e final de execução no log '''
    
    if not time_start:
        add_log("=========================== Inicializando logger ===========================\n")
        call_procedure(action='START')
        return time.time()

    else:
        add_log("=========================== Finalizando logger ===========================\n")
        return get_time(time_start)
    

def sum_steps(all_json_logs: list, total_time: float, all_time_logs: list):
    ''' Soma os valores de todos os steps e retorna o totalizador '''

    ext_sum = get_sum(all_json_logs, 'QT_TEMPO_EXTRACAO_SEG')
    tra_sum = get_sum(all_json_logs, 'QT_TEMPO_TRANSFORMACAO_SEG')
    loa_sum = get_sum(all_json_logs, 'QT_TEMPO_LOAD_SEG')

    final_times = [{
        '>>> ROTINA INTEIRA <<<': {'TIME': get_time(total_time)}, 
        'STEPS': [
            {'> EXTRACAO': get_time(ext_sum)},
            {'> TRANSFORMACAO': get_time(tra_sum)},
            {'> CARGA': get_time(loa_sum)}]
        }]
    
    return final_times + all_time_logs


def all_times_report(all_tables_times:list):
    ''' Relatório de tempo de execução '''

    def time_str(time:str):
        ''' Ajusta a string do tempo '''

        return f'|   {time}   |'


    def table_name(table:str, is_table:bool=False):
        ''' Ajusta a string com nomes dos jsons '''

        if is_table:
            table_limit = 36
            table_len = len(table)
            
            return f' ==> TEMPO TOTAL: {table}{" "*(table_limit - table_len)} |'

        table_len = len(table)
        table_limit = 53
        
        return f' {table}{" "*(table_limit - table_len)} |'
  

    line = '+--------------+-------------------------------------------------------+'

    add_log('==============>   RELATORIO DE TEMPO DE EXECUCAO   <===============\n', 'w')
    add_log(line, 'w')
    add_log(f'| TEMPO  TOTAL |                        TABELAS                        |', 'w')
    add_log(line, 'w')
    
    for table in all_tables_times: 
        t_table_name = list(table.keys())[0]
        add_log(f'{time_str(table[t_table_name]["TIME"])}{table_name(t_table_name, True)}', 'w')
        
        for step in table["STEPS"]:
            add_log(f'{time_str(list(step.values())[0])}{table_name(list(step.keys())[0])}', 'w')
            
        add_log(line, 'w')
    
    add_log('\n', 'w')


def get_steps_time(table_name: str, e_start: float, e_time: float, t_time: float, l_time: float):
    ''' Retorna o dicionario com os tempos calculados para cada etapa do ETL da tabela '''

    return {
        table_name: {
            'TIME': get_time(time.time() - e_start)}, 
            'STEPS': [
                {'EXTRACAO': get_time(e_time)}, 
                {'TRANSFORMACAO': get_time(t_time)}, 
                {'CARGA': get_time(l_time)}]
    }


def close_log(total_time: float, all_json_logs: list, extraction_date: str):
    ''' Fecha o arquivo de log e salva o tempo total da execução e lista de erros '''

    # ---- Gerando log GERAL ----
    ext_sum = get_sum(all_json_logs, 'QT_TEMPO_EXTRACAO_SEG')
    tra_sum = get_sum(all_json_logs, 'QT_TEMPO_TRANSFORMACAO_SEG')
    loa_sum = get_sum(all_json_logs, 'QT_TEMPO_LOAD_SEG')
    qtt_error = len(ERROR_LIST)
    python_lines = get_sum(all_json_logs, 'QT_LINHAS_PYTHON')
    end_date = get_date()

    full_routine = {
        'NM_ROTINA': c.r_name, 
        'NM_TABELA': 'CLOSE_LOG', 
        'NM_ORIGEM': None, 
        'DH_INICIO_EXECUCAO': extraction_date,
        'DH_FIM_EXECUCAO': end_date,
        'DS_TEMPO_EXTRACAO': get_time(ext_sum),
        'QT_TEMPO_EXTRACAO_SEG': ext_sum,
        'QT_LINHAS_ORIGEM': get_sum(all_json_logs, 'QT_LINHAS_ORIGEM'),
        'DS_TEMPO_TRANSFORMACAO': get_time(tra_sum),
        'QT_TEMPO_TRANSFORMACAO_SEG': tra_sum,
        'QT_LINHAS_PYTHON': python_lines,
        'DS_TEMPO_LOAD': get_time(loa_sum),
        'QT_TEMPO_LOAD_SEG': loa_sum,
        'DS_TEMPO_TOTAL': get_time(total_time),
        'QT_TEMPO_TOTAL_SEG': total_time,        
        'QT_ERROS': qtt_error}
    

    # ---- Add colunas EXTRAS ----
    final_list = [{**json, 'DS_TEMPO_TOTAL': None, 'QT_TEMPO_TOTAL_SEG': None, 'QT_ERROS': None} for json in all_json_logs]
    final_list.append(full_routine)   


    # ---- SAVE log ----
    columns = list(final_list[0].keys())
    columns_enum = [':' + str(i+1) for i in range(len(columns))]
    sql = f'INSERT INTO {c.o_meta} ({", ".join(columns)}) VALUES ({", ".join(columns_enum)})'

    data = [tuple(row[col] for col in columns) for row in final_list]

    with open_oracle_conn() as conn:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()


    # ---- Envia CARD ----
    send_card({
        'TITLE': c.r_name,
        'TITLE_SUBTITLE': f'Inicio: {to_str(extraction_date)} - Fim: {to_str(end_date)}',
        'MSG': f'|---> TEMPO TOTAL: {get_time(total_time)},\n|->Extração: {get_time(ext_sum)},\n|->Tranformação: {get_time(tra_sum)},\n|->Carga: {get_time(loa_sum)},\n|--->Erros: {qtt_error},\n|--->Tabelas: {len(full_routine)-1}'
    }, qtt_error > 0)


    # ---- Chamando PROCEDURE ----
    error_msg = f'Quantidade de errors: {qtt_error}' if qtt_error > 0 else None
    call_procedure(error_log=error_msg, row_count=python_lines) 


    # ---- FINALIZANDO rotina ----
    if qtt_error > 0:
        sys.exit(1)


def call_procedure(action: str='END', error_log: str=None, row_count: int=0):
    ''' Chama a procedure do Oracle para o registro do LOG pela Package '''

    params = {
        'p_package': 'PROJETO_CREDENCIADOS',
        'p_procedure': 'PROJETO_CREDENCIADOS',
        'p_command': 'CARGA',
        'p_action': action,
        'p_rowcount': row_count,
        'p_query': error_log
    }

    with open_oracle_conn() as conn:
        cursor = conn.cursor()
        cursor.callproc(
            'PC_DW_UTIL_CONTROLE.SP_LOG_COMM_NOVO',
            [
                params['p_package'],
                params['p_procedure'],
                params['p_command'],
                params['p_action'],
                params['p_rowcount'],
                params['p_query']
            ]
        )
        conn.commit()
