TABLES_NAME = {
    'area_info'               : 'AREA_INFO',
    'cronjob'                 : 'CRONJOB',
    'file_info'               : 'FILE_INFO',
    'form_area'               : 'FORM_AREA',
    'form_area_equipe'        : 'FORM_AREA_EQUIPE',
    'form_area_equipe_foco'   : 'FORM_AREA_EQUIPE_FOCO',
    'form_area_foco'          : 'FORM_AREA_FOCO',
    'form_foco'               : 'FORM_FOCO',
    'log'                     : 'LOG',
    'log_tipo'                : 'LOG_TIPO',
    'mail_info'               : 'MAIL_INFO',
    'savecontactform7_1'      : 'SAVECONTACT_FORM7_1',
    'savecontactform7_lookup' : 'SAVECONTACT_FORM7_LOOKUP',
    'seb_cf7_data'            : 'SEB_CF7_DATA',
    'seb_cf7_data_entry'      : 'SEB_CF7_DATA_ENTRY',
    'seb_commentmeta'         : 'SEB_COMMENTMETA',
    'seb_comments'            : 'SEB_COMMENTS',
    'seb_links'               : 'SEB_LINKS',
    'seb_masterslider_options': 'SEB_MASTERSLIDER_OPTIONS',
    'seb_masterslider_sliders': 'SEB_MASTERSLIDER_SLIDERS',
    'seb_options'             : 'SEB_OPTIONS',
    'seb_postmeta'            : 'SEB_POSTMETA',
    'seb_posts'               : 'SEB_POSTS',
    'seb_term_relationships'  : 'SEB_TERM_RELATIONSHIPS',
    'seb_term_taxonomy'       : 'SEB_TERM_TAXONOMY',
    'seb_termmeta'            : 'SEB_TERMMETA',
    'seb_terms'               : 'SEB_TERMS',
    'seb_usermeta'            : 'SEB_USERMETA',
    'seb_users'               : 'SEB_USERS',
}

CLOB_COLUMNS = {
    'BI_STG.TEMP_CRD_CRONJOB': {
        'cd': [
            'CD_ID',
            'CD_POST'],
        'column': [
            'DS_TEXTO',
            'DS_TITULO',
            'DS_ANEXO',
            'DS_EMAIL']},
    
    'BI_STG.TEMP_CRD_LOG': {
        'cd': [
            'CD_ID',
            'CD_POST'],
        'column': [
            'DS_TEXTO']},
    
    'BI_STG.TEMP_CRD_SEB_COMMENTS': {
        'cd': [
            'CD_COMMENT_ID',
            'CD_POST'],
        'column':[
            'DS_CONTENT']},

    'BI_STG.TEMP_CRD_SEB_MASTERSLIDER_SLID': {
        'cd': [
            'CD_ID'],
        'column':[
            'DS_CUSTOM_STYLES',
            'DS_CUSTOM_FONTS',
            'DS_PARAMS']},

    'BI_STG.TEMP_CRD_SEB_OPTIONS': {
        'cd': [
            'CD_OPTION_ID'],
        'column':[
            'DS_OPTION_VALUE']},

    'BI_STG.TEMP_CRD_SEB_POSTS': {
        'cd': [
            'CD_ID',
            'CD_AUTHOR'],
        'column':[
            'DS_CONTENT',
            'DS_TITLE',
            'DS_EXCERPT',
            'DS_TO_PING',
            'DS_PINGED',
            'DS_CONTENT_FILTERED']},

    'BI_STG.TEMP_CRD_SEB_TERM_TAXONOMY': {
        'cd': [
            'CD_TERM_TAXONOMY_ID',
            'CD_TERM_ID'],
        'column':[
            'DS_DESCRIPTION']}
}

REORDER_COLUMNS = { 
    'BI_STG.TEMP_CRD_CRONJOB': [
        'CD_ID',
        'CD_POST',        
        'TP_STATUS',        
        'DH_CRONJOB',        
        'TP_CRONJOB',
        'DH_CRONJOB_INC',
        'DS_ANEXO_NOME',
        'DS_TEXTO',
        'DS_TITULO',
        'DS_ANEXO',
        'DS_EMAIL'],
    
    'BI_STG.TEMP_CRD_LOG': [
        'CD_ID',
        'CD_POST',         
        'DH_LOG',
        'CD_USER',
        'TP_LOG', 
        'NR_CPF', 
        'TP_AREA', 
        'TP_SUBAREA',
        'DS_FOCO', 
        'TP_STATUS', 
        'DS_FILE',
        'DS_TEXTO'],

    'BI_STG.TEMP_CRD_SEB_COMMENTS': [
        'CD_COMMENT_ID',
        'CD_POST',
        'DS_AUTHOR',
        'DS_AUTHOR_EMAIL',
        'DS_AUTHOR_URL',
        'DS_AUTHOR_IP',
        'DH_COMMENT',
        'DH_COMMENT_GMT',        
        'CD_KARMA',
        'DS_APPROVED',
        'DS_AGENT',
        'DS_TYPE',
        'CD_PARENT',
        'CD_USER',
        'DS_CONTENT'],

    'BI_STG.TEMP_CRD_SEB_MASTERSLIDER_SLID': [
        'CD_ID',
        'DS_TITLE',
        'DS_TYPE',
        'CD_SLIDE_NUM',
        'DH_CREATED',
        'DH_MODIFIED',                
        'DS_STATUS',
        'DS_CUSTOM_STYLES',
        'DS_CUSTOM_FONTS',
        'DS_PARAMS'],

    'BI_STG.TEMP_CRD_SEB_OPTIONS': [
        'CD_OPTION_ID',
        'DS_OPTION_NAME',
        'DS_AUTOLOAD',
        'DS_OPTION_VALUE'],

    'BI_STG.TEMP_CRD_SEB_POSTS': [
        'CD_ID',
        'CD_AUTHOR',
        'DH_POST',
        'DH_POST_GMT',
        'DS_POST_STATUS',
        'DS_COMMENT_STATUS',
        'DS_PING_STATUS',
        'DS_POST_PASSWORD',
        'DS_POST_NAME',        
        'DH_MODIFIED',
        'DH_MODIFIED_GMT',        
        'CD_POST_PARENT',
        'DS_GUID',
        'CD_MENU_ORDER',
        'DS_TYPE',
        'DS_MIME_TYPE',
        'NR_COMMENT_COUNT',
        'DS_CONTENT',
        'DS_TITLE',
        'DS_EXCERPT',
        'DS_TO_PING',
        'DS_PINGED',
        'DS_CONTENT_FILTERED'],

    'BI_STG.TEMP_CRD_SEB_TERM_TAXONOMY': [
        'CD_TERM_TAXONOMY_ID',
        'CD_TERM_ID',
        'DS_TAXONOMY',        
        'CD_PARENT',
        'NR_COUNT',
        'DS_DESCRIPTION']
}

TABLES_COLUMNS = {
    'area_info': {
        'id'         : 'CD_ID',
        'post_id'    : 'CD_POST',
        'job_id'     : 'CD_JOB',
        'area'       : 'DS_AREA',
        'subarea'    : 'DS_SUBAREA',
        'consultoria': 'DS_CONSULTORIA',
        'instrutoria': 'DS_INSTRUTORIA',
        'conteudista': 'DS_CONTEUDISTA',
        'tutoria'    : 'DS_TUTORIA',
        'coaching'   : 'DS_COACHING',
        'orientacao' : 'DS_ORIENTACAO',
        'equipe_cpf' : 'NR_EQUIPE_CPF',
        'equipe_nome': 'NM_EQUIPE'},
    
    'cronjob': {
        'ID'        : 'CD_ID',
        'post_id'   : 'CD_POST',
        'texto'     : 'DS_TEXTO',
        'status'    : 'TP_STATUS',
        'titulo'    : 'DS_TITULO',
        'data'      : 'DH_CRONJOB',
        'email'     : 'DS_EMAIL',
        'tipo'      : 'TP_CRONJOB',
        'data_inc'  : 'DH_CRONJOB_INC',
        'anexo'     : 'DS_ANEXO',
        'anexo_nome': 'DS_ANEXO_NOME'},
    
    'file_info': {
        'id'         : 'CD_ID',
        'post_id'    : 'CD_POST',
        'job_id'     : 'CD_JOB',
        'tipo'       : 'DS_TIPO',
        'status'     : 'DS_STATUS',
        'equipe_cpf' : 'NR_EQUIPE_CPF',
        'equipe_nome': 'NM_EQUIPE'},
    
    'form_area': {
        'id'     : 'CD_ID',
        'post_id': 'CD_POST',
        'area'   : 'TP_AREA', 
        'subarea': 'TP_SUBAREA'},

    'form_area_equipe': {
        'id'     : 'CD_ID',
        'post_id': 'CD_POST',
        'cpf'    : 'NR_AREA_CPF',
        'area'   : 'TP_AREA', 
        'subarea': 'TP_SUBAREA'},

    'form_area_equipe_foco': {
        'id'                 : 'CD_ID',
        'form_area_equipe_id': 'CD_FORM_AREA_EQUIPE',
        'foco'               : 'DS_FOCO',
        'status'             : 'TP_STATUS'},

    'form_area_foco': {
        'id'          : 'CD_ID',
        'form_area_id': 'CD_FORM_AREA',
        'foco'        : 'DS_FOCO',
        'status'      : 'TP_STATUS'},

    'form_foco': {
        'id'     : 'CD_ID',
        'post_id': 'CD_POST',
        'foco'   : 'DS_FOCO',
        'status' : 'TP_STATUS'},

    'log': {
        'ID'     :'CD_ID',
        'post_id':'CD_POST',
        'texto'  :'DS_TEXTO', 
        'data'   :'DH_LOG',
        'user_id':'CD_USER',
        'tipo'   :'TP_LOG', 
        'cpf'    :'NR_CPF', 
        'area'   :'TP_AREA', 
        'subarea':'TP_SUBAREA',
        'foco'   :'DS_FOCO', 
        'status' :'TP_STATUS', 
        'file'   :'DS_FILE'},

    'log_tipo': {
        'id'       :'CD_ID',
        'descricao':'DS_LOG'},
    
    'mail_info': {
        'id'                 : 'CD_ID',
        'post_id'            : 'CD_POST',
        'job_id'             : 'CD_JOB',
        'data_cadastro'      : 'DH_CADASTRO',
        'data_confirmado'    : 'DH_CONFIRMADO',
        'cnpj'               : 'NR_CNPJ',
        'razao'              : 'NM_RAZAO',
        'cidade'             : 'NM_CIDADE',
        'email_empresa'      : 'DS_EMAIL_EMPRESA',
        'nome_representante' : 'DS_NOME_REPRESENTANTE',
        'email_representante': 'DS_EMAIL_REPRESENTANTE',
        'status'             : 'DS_STATUS'},
    
    'savecontactform7_1': {
        'id'                   : 'CD_ID',
        'created_on'           : 'DH_CRIACAO',
        'razaosocial'          : 'DS_RAZAO_SOCIAL',
        'nomefantasia'         : 'DS_NOME_FANTASIA',
        'emailempresa'         : 'DS_EMAIL_EMPRESA',
        'telefoneempresa'      : 'NR_TELEFONE_EMPRESA',
        'cnpjempresa'          : 'NR_CNPJ_EMPRESA',
        'naturezajuridica'     : 'DS_NATUREZA_JURIDICA',
        'dataabertura'         : 'DH_ABERTURA',
        'optantesimples'       : 'DS_OPTANTE_SIMPLES',
        'cnae'                 : 'NR_CNAE',
        'objetosocial'         : 'DS_OBJETO_SOCIAL',
        'enderecoempresa'      : 'DS_ENDERECO_EMPRESA',
        'complementoempresa'   : 'DS_END_COMPLEMENTO_EMPRESA',
        'bairroempresa'        : 'DS_END_BAIRRO_EMPRESA',
        'cidadeempresa'        : 'DS_CIDADE_EMPRESA',
        'estadoempresa'        : 'DS_ESTADO_EMPRESA',
        'cepempresa'           : 'NR_CEP_EMPRESA',
        'nomerepresentante'    : 'DS_NOME_REPRESENTANTE',
        'emailrepresentante'   : 'DS_EMAIL_REPRESENTANTE',
        'rgrepresentante'      : 'NR_RG_REPRESENTANTE',
        'orgaoexpedidor'       : 'DS_ORGAO_EXPEDIDOR',
        'cpfrepresentante'     : 'NR_CPF_REPRESENTANTE',
        'celularrepresentante' : 'NR_CELULAR_REPRESENTANTE',
        'telefonerepresentante': 'NR_TELEFONE_REPRESENTANTE',
        'arquivos'             : 'DS_ARQUIVOS'},

    'savecontactform7_lookup': {
        'lookup_id'              : 'CD_LOOKUP',
        'CFDBA_tbl_name'         : 'NM_CFDBA_TBL_NAME',
        'CF7_created_title'      : 'DS_CF7_CREATED_TITLE',
        'CF7_created_date'       : 'DH_CF7_CREATED_DATE',
        'CF7_version'            : 'NM_CF7_VERSION',
        'CF7_form_id'            : 'CD_CF7_FORM_ID',
        'CF7_from_wpposts_or_tbl': 'DS_CF7_FROM_WPPOSTS_OR_TBL',
        'CF7_removed_flag'       : 'DS_CF7_REMOVED_FLAG'},

    'seb_cf7_data': {
        'id'     : 'CD_ID',
        'created': 'DH_CREATED'},

    'seb_cf7_data_entry': {
        'id'     : 'CD_ID',
        'cf7_id' : 'CD_CF7_ID',
        'data_id': 'CD_DATA',
        'name'   : 'DS_NAME',
        'value'  : 'DS_VALUE'},

    'seb_commentmeta': {
        'meta_id'    : 'CD_META_ID',
        'comments_id': 'CD_COMMENT_ID',
        'meta_key'   : 'DS_META_KEY',
        'meta_value' : 'DS_META_VALUE'},

    'seb_comments': {
        'comment_ID'          : 'CD_COMMENT_ID',
        'comment_post_ID'     : 'CD_POST',
        'comment_author'      : 'DS_AUTHOR',
        'comment_author_email': 'DS_AUTHOR_EMAIL',
        'comment_author_url'  : 'DS_AUTHOR_URL',
        'comment_author_IP'   : 'DS_AUTHOR_IP',
        'comment_date'        : 'DH_COMMENT',
        'comment_date_gmt'    : 'DH_COMMENT_GMT',
        'comment_content'     : 'DS_CONTENT',
        'comment_karma'       : 'CD_KARMA',
        'comment_approved'    : 'DS_APPROVED',
        'comment_agent'       : 'DS_AGENT',
        'comment_type'        : 'DS_TYPE',
        'comment_parent'      : 'CD_PARENT',
        'user_id'             : 'CD_USER'},

    'seb_links': {
        'link_id'         : 'CD_LINK_ID',
        'link_url'        : 'DS_URL',
        'link_name'       : 'DS_NAME',
        'link_image'      : 'DS_IMAGE',
        'link_target'     : 'DS_TARGET',
        'link_description': 'DS_DESCRIPTION',
        'link_visible'    : 'DS_VISIBLE',
        'link_owner'      : 'CD_OWNER',
        'link_rating'     : 'CD_RATING',
        'link_updated'    : 'DH_UPDATED',
        'link_rel'        : 'DS_REL',
        'link_notes'      : 'DS_NOTES',
        'link_rss'        : 'DS_RSS'},

    'seb_masterslider_options': {
        'ID'          : 'CD_ID',
        'option_name' : 'DS_OPTION_NAME',
        'option_value': 'DS_OPTION_VALUE'},

    'seb_masterslider_sliders': {
        'ID'           : 'CD_ID',
        'title'        : 'DS_TITLE',
        'type'         : 'DS_TYPE',
        'slides_num'   : 'CD_SLIDE_NUM',
        'date_created' : 'DH_CREATED',
        'date_modified': 'DH_MODIFIED',
        'params'       : 'DS_PARAMS',
        'custom_styles': 'DS_CUSTOM_STYLES',
        'custom_fonts' : 'DS_CUSTOM_FONTS',
        'status'       : 'DS_STATUS'},

    'seb_options': {
        'option_id'   : 'CD_OPTION_ID',
        'option_name' : 'DS_OPTION_NAME',
        'option_value': 'DS_OPTION_VALUE',
        'autoload'    : 'DS_AUTOLOAD'},

    'seb_postmeta': {
        'meta_id'   : 'CD_META_ID',
        'post_id'   : 'CD_POST',
        'meta_key'  : 'DS_META_KEY',
        'meta_value': 'DS_META_VALUE'},

    'seb_posts': {
        'ID'                   : 'CD_ID',
        'post_author'          : 'CD_AUTHOR',
        'post_date'            : 'DH_POST',
        'post_date_gmt'        : 'DH_POST_GMT',
        'post_content'         : 'DS_CONTENT',
        'post_title'           : 'DS_TITLE',
        'post_excerpt'         : 'DS_EXCERPT',
        'post_status'          : 'DS_POST_STATUS',
        'comment_status'       : 'DS_COMMENT_STATUS',
        'ping_status'          : 'DS_PING_STATUS',
        'post_password'        : 'DS_POST_PASSWORD',
        'post_name'            : 'DS_POST_NAME',
        'to_ping'              : 'DS_TO_PING',
        'pinged'               : 'DS_PINGED',
        'post_modified'        : 'DH_MODIFIED',
        'post_modified_gmt'    : 'DH_MODIFIED_GMT',
        'post_content_filtered': 'DS_CONTENT_FILTERED',
        'post_parent'          : 'CD_POST_PARENT',
        'guid'                 : 'DS_GUID',
        'menu_order'           : 'CD_MENU_ORDER',
        'post_type'            : 'DS_TYPE',
        'post_mime_type'       : 'DS_MIME_TYPE',
        'comment_count'        : 'NR_COMMENT_COUNT'},

    'seb_term_relationships': {
        'object_id'       : 'CD_OBJECT_ID',
        'term_taxonomy_id': 'CD_TERM_TAXONOMY_ID',
        'term_order'      : 'NR_TERM_ORDER'},

    'seb_term_taxonomy': {
        'term_taxonomy_id': 'CD_TERM_TAXONOMY_ID',
        'term_id'         : 'CD_TERM_ID',
        'taxonomy'        : 'DS_TAXONOMY',
        'description'     : 'DS_DESCRIPTION',
        'parent'          : 'CD_PARENT',
        'count'           : 'NR_COUNT'},

    'seb_termmeta': {
        'meta_id'   : 'CD_META_ID',
        'term_id'   : 'CD_TERM',
        'meta_key'  : 'DS_META_KEY',
        'meta_value': 'DS_META_VALUE'},

    'seb_terms': {
        'term_id'   : 'CD_TERM_ID',
        'name'      : 'DS_NAME',
        'slug'      : 'DS_SLUG',
        'term_group': 'CD_TERM_GROUP'},

    'seb_usermeta': {
        'umeta_id'  : 'CD_USER_META_ID',
        'user_id'   : 'CD_USER_ID',
        'meta_key'  : 'DS_META_KEY',
        'meta_value': 'DS_META_VALUE'},

    'seb_users': {
        'ID'                 : 'CD_ID',
        'user_login'         : 'DS_LOGIN',
        'user_pass'          : 'DS_PASS',
        'user_nicename'      : 'DS_NICE_NAME',
        'user_email'         : 'DS_EMAIL',
        'user_url'           : 'DS_URL',
        'user_registered'    : 'DH_REGISTERED',
        'user_activation_key': 'DS_ACTIVATION_KEY',
        'user_status'        : 'CD_STATUS',
        'display_name'       : 'DS_DISPLAY_NAME'}
}
