from pymongo import MongoClient
from pprint import pprint

# Conecte-se ao MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Substitua pelo seu URI do MongoDB, se necessário

# Selecione o banco de dados
db = client['nome_do_banco']  # Substitua pelo nome do seu banco de dados

# Selecione a coleção
#collection = db['acre']  # Substitua pelo nome da sua coleção

print(db.acre.estado)

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
