import warnings
from managers.base_manager import base as b

#Filtra os avisos que contêm a mensagem "error reading bcrypt version" e os ignora.
warnings.filterwarnings("ignore", message=".*error reading bcrypt version.*")


class Config():
    #region Oracle
    o_auth = b('')
    o_path = b('')
    o_db = b('')
    o_str = f'{o_auth}/{o_auth}@{o_path}/{o_db}'
    o_log = b('')
    o_meta = b('')

    #region API
    a_grant = b('')
    a_id = b('')
    a_secret = b('')
    a_purl = b('')
    a_murl = b('')
    a_sales = b('')
    a_face = b('')
    a_face2 =  b('')

    #region Teams
    teams = b('')

    #region Gogs
    g_url = b('')
    g_rep_owner = b('')
    g_rep_name = b('')
    g_branch = b('')
    g_directory = b('')
    g_file = b('')
    g_header = None

    #region Table
    s_prefix = 'RD_SCL_'
    s_tables = ['SALES_FORCE', 'SALES_FORCE_FACE', 'SALES_FORCE_FACE_V2']
    s_table = 'SALES_FORCE'

    # region Rotina
    r_name = '20_REDE_SOCIAL_SALES_FORCE'
    r_procedure = 'PROJETO_REDE_SOCIAL_SALES_FORCE'

config = Config()
