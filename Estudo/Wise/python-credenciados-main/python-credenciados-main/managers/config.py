import warnings
from managers.base_manager import base as b

warnings.filterwarnings("ignore", message=".*error reading bcrypt version.*")


class Config():
    #region Oracle
    o_auth = b('')
    o_path = b('')
    o_db = b('')
    o_str = f'{o_auth}/{o_auth}@{o_path}/{o_db}'
    o_log = b('')
    o_meta = b('')

    #region MySql
    m_user = b('')
    m_auth = b('')
    m_path = b('')
    m_db = b('')
    m_str = f"mysql+pymysql://{m_user}:{m_auth}@{m_path}/{m_db}"

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
    s_prefix = 'CRD_'

    # region Rotina
    r_name = '20_CREDENCIADOS'

config = Config()

