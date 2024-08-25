from pymongo import MongoClient
from pprint import pprint
import mysql.connector



# Conecte ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Primeiro_teste']  # Substitua pelo nome do seu banco de dados
collection = db['usuarios']  # Substitua pelo nome da sua coleção

# Extrair dados do MongoDB
documentos = collection.find()  # Pode usar um filtro se necessário

for usuario in documentos :
    print(usuario['estado'])




exit()


# Conecte ao MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="blog"
)
cursor = conn.cursor()



# Criar um cursor para executar consultas
cursor = conn.cursor()

# Escrever sua consulta SQL
consulta_sql = "SELECT * FROM users;"

# Executar a consulta
cursor.execute(consulta_sql)

# Obter os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar o cursor e a conexão
cursor.close()
conn.close()



















# Insira os dados no MySQL
query = "INSERT INTO nome_da_tabela_mysql (coluna1, coluna2, coluna3) VALUES (%s, %s, %s)"

# Iterando sobre os documentos do MongoDB e inserindo no MySQL
for documento in documentos:
    # Substitua 'coluna_mongo1', 'coluna_mongo2' etc. pelos campos no seu documento MongoDB
    valores = (
        documento.get('coluna_mongo1'),
        documento.get('coluna_mongo2'),
        documento.get('coluna_mongo3')
    )
    cursor.execute(query, valores)

# Confirmar as mudanças no MySQL
conn.commit()

# Fechar conexões
cursor.close()
conn.close()
client.close()





























exit()


for usuario in db['usuarios'] :
    print(usuario['estado'])



print(db['usuarios'])
print('teste')

# Consulte todos os documentos na coleção
#documents = collection.find()

'''
# Imprima os documentos
for doc in documents:
    #pprint(doc)
    pass

'''


'''
estados = [
    {"estado": "Acre", "capital": "Rio Branco", "habitantes": 894470},
    {"estado": "Alagoas", "capital": "Maceió", "habitantes": 3365351},
    {"estado": "Amapá", "capital": "Macapá", "habitantes": 861773},
    {"estado": "Amazonas", "capital": "Manaus", "habitantes": 4207714},
    {"estado": "Bahia", "capital": "Salvador", "habitantes": 14812617},
    {"estado": "Ceará", "capital": "Fortaleza", "habitantes": 9240580},
    {"estado": "Distrito Federal", "capital": "Brasília", "habitantes": 3094325},
    {"estado": "Espírito Santo", "capital": "Vitória", "habitantes": 4108508},
 
  
    {"estado": "Goiás", "capital": "Goiânia", "habitantes": 7113540},
    {"estado": "Maranhão", "capital": "São Luís", "habitantes": 7153262},
    {"estado": "Mato Grosso", "capital": "Cuiabá", "habitantes": 3567234},
    {"estado": "Mato Grosso do Sul", "capital": "Campo Grande", "habitantes": 2884297},
    {"estado": "Minas Gerais", "capital": "Belo Horizonte", "habitantes": 21411923},
    {"estado": "Pará", "capital": "Belém", "habitantes": 8777124},
    {"estado": "Paraíba", "capital": "João Pessoa", "habitantes": 4059905},
    {"estado": "Paraná", "capital": "Curitiba", "habitantes": 11963273},
    {"estado": "Pernambuco", "capital": "Recife", "habitantes": 9714398},
    {"estado": "Piauí", "capital": "Teresina", "habitantes": 3289290},
    {"estado": "Rio de Janeiro", "capital": "Rio de Janeiro", "habitantes": 17366189},
    {"estado": "Rio Grande do Norte", "capital": "Natal", "habitantes": 3560903},
    {"estado": "Rio Grande do Sul", "capital": "Porto Alegre", "habitantes": 11422973},
    {"estado": "Rondônia", "capital": "Porto Velho", "habitantes": 1845155},
    {"estado": "Roraima", "capital": "Boa Vista", "habitantes": 652713},
    {"estado": "Santa Catarina", "capital": "Florianópolis", "habitantes": 7372110},
    {"estado": "São Paulo", "capital": "São Paulo", "habitantes": 46649132},
    {"estado": "Sergipe", "capital": "Aracaju", "habitantes": 2378187},
    {"estado": "Tocantins", "capital": "Palmas", "habitantes": 1607363}
]

# Inserir cada estado em uma coleção separada
for estado in estados:
    collection_name = estado["estado"].replace(" ", "_").lower()
    collection = db[collection_name]
    collection.insert_one(estado)

print("Importação concluída com sucesso!")
'''
