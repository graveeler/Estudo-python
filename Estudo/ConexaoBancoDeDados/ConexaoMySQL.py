import mysql.connector


# Conectando ao banco de dados
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="blog"
)

# Criando um cursor
cur = con.cursor()

# Executando uma consulta SQL
cur.execute('SELECT * FROM posts')

# Obtendo resultados
resultados = cur.fetchall()

# Fechando a conexão
con.close()

print(resultados)




