# PYTHON SALES FORCE

## Descrição

Este projeto é uma aplicação que tem como objetivo automatizar a extração das informaçòes pela API do Sales Force e fazer a carga do mesmo em sua respectiva tabela no Banco Oracle de Stage.

## Funcionalidades

- **Extração das informações**: Realiza a extração de uma fonte e adiciona na outra.
- **Transformação das informações**: Realiza as transformações necessárias nos dados a fim de adaptar a estrutura SQL.
- **Carga das informações**: Realiza a carga da tabela em Stage apenas se houver sucesso na extração e transformação.

## Estrutura do Projeto

O projeto é composto pelos seguintes diretórios e arquivos:

- `extras/`: Contém os mapeamentos para diferentes aspectos do projeto.
  - `maps.py`: Mapeamento das colunas.
- `logs/`: Diretório onde os logs de execução são registrados.
- `managers/`: Contém os gerenciadores (managers) para diferentes aspectos do projeto.
  - `base_manager.py`: Centraliza a integração das informações de configuração.
  - `config.py`: Centraliza todos os parâmetros necessários para o funcionamento da aplicação, incluindo links e informações de banco de dados.
  - `database_manager.py`: Centraliza todas as funções e operações relacionadas à interação com os bancos de dados.
  - `file_manager.py`: Centraliza todas as funções que envolvem a normalização e padrões das informações.
  - `gogs_manager.py`: Centraliza as funções que envolvem a extraçào dos schemas das tabelas do Gogs.
  - `integration_manager.py`: Contém o context manager responsável por abrir e fechar a conexão com o banco de dados.
  - `log_manager.py`: Centraliza todas as funções relacionadas ao registro de log do projeto.  
  - `teams_manager.py`: Centraliza todas as funções e operações relacionadas às interações com o Microsoft Teams.  
- `routines/`: Contém os executáveis do projeto.
  - `sales_force.py`: Contém a rotina que faz a carga em stage, responsável por extrair dados do Sales Force e salvar essas informações no banco de dados de stage.
- `README.md`: Documentação do projeto (este arquivo).

## **Regras e Comentários Gerais**
| Num | Data | Desenvolvedor | Observação
|---|---|---|---|
| 1 | 01/08/2024 | Leticia Figueiredo | É necessário chamar a procedure de controle sempre no início e no final da rotina. Como existem cenários em que a rotina pode ser encerrada forçadamente, mesmo nesses casos, a procedure precisa ser chamada, informando os erros da execução.
| 2 | 01/08/2024 | Leticia Figueiredo | Foi adicionado ao log_exception o envio do erro para a tabela de controle de erros. Dessa forma, os erros podem ser analisados sem a necessidade de acessar diretamente o servidor.
| 3 | 01/08/2024 | Leticia Figueiredo | Durante a criação da tabela temporária, os comandos são enviados individualmente por meio de um laço de repetição, pois o Oracle não aceita o envio de múltiplos comandos em uma única string.
| 4 | 01/08/2024 | Leticia Figueiredo | O esquema das tabelas é extraído do GOGS para garantir a transparência e o versionamento do schema das tabelas.
| 5 | 01/08/2024 | Leticia Figueiredo | Se não retornar nenhum dado da API, a extração será ignorada. Em outras palavras, as informações na tabela não serão deletadas na Stage. Dessa forma, garantimos que, em caso de erro na fonte, o último dado histórico permanecerá disponível.
|   |   |   |   |

## **Atualizações**
| Num | Data | Desenvolvedor | Alterações
|---|---|---|---|
| 1 | 01/08/2024 | Leticia Figueiredo | Criação do Script |
| 2 | 05/08/2024 | Leticia Figueiredo | Alterando logica do Teams para se adaptar ao Workflow |
| 3 | 12/08/2024 | Leticia Figueiredo | Adicionando novo id de busca na API e adaptando a logica para popular mais de uma tabela |
|   |   |   |   |
