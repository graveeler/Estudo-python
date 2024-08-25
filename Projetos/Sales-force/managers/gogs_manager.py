import requests, base64
from managers.config import config as c
from managers.log_manager import log_exception
from managers.file_manager import get_temp_name

# O que são esses arquivos sql?

def get_gogs_files():
    ''' Extrai o arquivo mais recente dos arquivos sql das tabelas de Stage do Gogs '''
    
    try:
        # ---- LISTANDO .sql ----
        try:
            url = f'{c.g_url}/repos/{c.g_rep_owner}/{c.g_rep_name}/contents/{c.g_directory}?ref={c.g_branch}'
            c.g_header = {'Authorization': f'token {c.g_file}'}
            response = requests.get(url, headers=c.g_header)
            response.raise_for_status()            
            
            all_files = response.json()   
            # Filtrando apenas os arquivos que tem o prefixo CRD no nome        
            all_files = {f['name'].split('.')[0]: f['content'] for f in all_files if f['name'].startswith(c.s_prefix)}
        
        except:
            raise Exception('| CONEXAO COM GOGS | Falha ao listar .sql no Gogs')
        
        
        # ---- MANIPULANDO .sql ----
        try:
            final_dict = {}
            for table_name, content in all_files.items():
                if table_name not in [f'{c.s_prefix}{t}' for t in c.s_tables]:
                    continue
                
                try:
                    decoded_content = base64.b64decode(content).decode('utf-8')
                    new_content = adjust_sql(decoded_content)
                    final_dict[f'{c.o_auth}.{table_name}'] = new_content
                
                except: # Try interno e individual porque se um der problema, mata a rotina ignorando todas os demais que deram certo
                    raise Exception()
                
            return final_dict

        except:
            raise Exception(f'| EXTRAINDO | Falha ao extrair content da tabela: {table_name}')  
        
    except Exception as e:
        log_exception(e, '| GOGS | Extraindo/Manipulando conteúdo do .sql', {
            'TITLE': 'EXTRAINDO SCHEMAS GOGS',
            'TITLE_SUBTITLE': 'Interação com o Gogs',
            'MSG': 'Falha na extração ou manipulação dos arquivos do Gogs'}, exit=True) # Força o encerramento da rotina


def adjust_sql(decoded_content: str):
    ''' Altera o conteúdo do schema removendo o DROP TABLE, adicionando o prefixo TEMP_ no nome da tabela e limitando o nome a 30 caracteres '''

    # Quebrando as linhas do arquivo
    if '\r\n' in decoded_content:
        lines = decoded_content.split('\r\n')

    elif '\n' in decoded_content:
        lines = decoded_content.split('\n')


    # ---- REMOVENDO o comentario ----
    processed_lines = [line for line in lines if not line.strip().lower().startswith('-- grant')]


    # ---- REMOVENDO o DROP ----
    processed_lines = [line for line in processed_lines if not line.strip().lower().startswith('drop table')]


    # ---- RENOMEANDO tabela ----    
    create_table_line = next(line for line in processed_lines if line.strip().lower().startswith('create table')) # Pegando linha com comando CREATE TABLE
    full_table_name = create_table_line.split()[-1] # Pegando o nome da tabela
    sep_full_table_name = full_table_name.split('.') # Separando o db e tabela

    new_full_table_name = get_temp_name(sep_full_table_name[0], sep_full_table_name[1])


    # ---- Atualizando o CREATE TABLE ----
    processed_lines = [line.replace(full_table_name, new_full_table_name) if line.strip().lower().startswith('create table') else line for line in processed_lines]


    # ---- Atualizando os GRANTS ----
    processed_lines = [line.replace(full_table_name, new_full_table_name) if 'grant select' in line.lower() else line for line in processed_lines]


    # ---- COMBINANDO linhas ----
    updated_content = '\r\n'.join(processed_lines)

    return updated_content
