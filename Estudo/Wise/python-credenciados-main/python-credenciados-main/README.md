# PYTHON CREDENCIADOS

## Descrição

Este projeto é uma aplicação que tem como objetivo automatizar a extração de todo o conteúdo do database CREDENCIADOS do MySql e fazer a carga do mesmo em suas respectivas tabelas no Banco Oracle de Stage.

## Funcionalidades

- **Extração das informações**: Realiza a extração de uma fonte e adicona na outra.
- **Transformação das informações**: Realiza as transformações necessárias nos dados a fim de adaptar a estrutura SQL entre os dois bancos.
- **Carga das informações**: Realiza a carga das tabelas em Stage apenas se houver sucesso na extração e transformação de todas as tabelas.

## Estrutura do Projeto

O projeto é composto pelos seguintes diretórios e arquivos:

- `extras/`: Contém os mapeamentos para diferentes aspectos do projeto.
  - `maps.py`: Mapeamento das tabelas e colunas.
- `managers/`: Contém os gerenciadores (managers) para diferentes aspectos do projeto.
  - `base_manager.py`: Centraliza a integração das informações de configuração.
  - `config.py`: Centraliza todos os parâmetros necessários para o funcionamento da aplicação, incluindo links e informações dos bancos de dados.
  - `database_manager.py`: Centraliza todas as funções e operações relacionadas à interação com os bancos de dados.
  - `file_manager.py`: Centraliza todas as funções que envolvem a normalização e padrões das informações.
  - `integration_manager.py`: Contém o context manager responsável por abrir e fechar a conexão com o banco de dados.
  - `log_manager.py`: Centraliza todas as funções relacionadas ao registro de log do projeto.  
  - `teams_manager.py`: Centraliza todas as funções e operações relacionadas às interações com o Microsoft Teams.  
- `logs/`: Diretório onde os logs de execução são registrados.
- `routines/`: Contém os executáveis do projeto.
  - `accredited.py`: Contém a rotina que faz a carga em stage, responsável por extrair dados do MySQL e salvar essas informações no banco de dados de stage.
- `README.md`: Documentação do projeto (este arquivo).

## **Regras e Comentários Gerais**
| Num | Data | Desenvolvedor | Observação
|---|---|---|---|
| 1 | 29/07/2024 | Aparecido Jr | Foi decidido que os dados da Carga só serão inseridos na etapa de Stage se todas as tabelas forem processadas com sucesso. Caso contrário, nenhuma inserção será realizada. Por isso, utilizamos tabelas temporárias para a inserção dos dados inicialmente.
| 2 | 29/07/2024 | Leticia Figueiredo | É necessário chamar a procedure de controle sempre no início e no final da rotina. Como existem cenários em que a rotina pode ser encerrada forçadamente, mesmo nesses casos, a procedure precisa ser chamada, informando os erros da execução.
| 3 | 29/07/2024 | Leticia Figueiredo | Foi adicionado ao log_exception o envio do erro para a tabela de controle de erros. Dessa forma, os erros podem ser analisados sem a necessidade de acessar diretamente o servidor.
| 4 | 29/07/2024 | Leticia Figueiredo | Devido ao tamanho e aos problemas encontrados durante a inserção de tabelas com colunas CLOB, essas colunas são inseridas individualmente por meio de um comando UPDATE.
| 5 | 29/07/2024 | Leticia Figueiredo | Durante a criação da tabela temporária, os comandos são enviados individualmente por meio de um laço de repetição, pois o Oracle não aceita o envio de múltiplos comandos em uma única string.
| 6 | 29/07/2024 | Leticia Figueiredo | O esquema das tabelas é extraído do GOGS para garantir a transparência e o versionamento do schema das tabelas.
| 7 | 29/07/2024 | Aparecido Jr | Foi decidido que, se uma tabela estiver populada na Stage, mas todos os dados na fonte forem excluídos, essa tabela será ignorada. Em outras palavras, as informações na tabela não serão deletadas na Stage. Dessa forma, garantimos que, em caso de erro na fonte, o último dado histórico permanecerá disponível.
|   |   |   |   |

## **Atualizações**
| Num | Data | Desenvolvedor | Alterações
|---|---|---|---|
| 1 | 29/07/2024 | Leticia Figueiredo | Criação do Script |
| 2 | 31/07/2024 | Leticia Figueiredo | Criação do BPMN |
|   |   |   |   |
