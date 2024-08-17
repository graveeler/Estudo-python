# Estudar o Type Hint

def teste():
    print('chamei funcao')
    
teste()



def testeComParametros(a, b, c):
    print(f'chamei funcao com parametro resultado: {a+b+c}')
         
testeComParametros(10,20,30)



def testeComParametrosERetorno(a, b, c):
    return a+b+c
     
result = testeComParametrosERetorno(30,20,30)

print(result)


# Função usando o type Hint, tipamos o parametro e definimos o tipo do retorno
# Essa tipagem nao esta funcionando... ele aceita qualquer tipo de retorno.

def testeTypeHint(lista : list) -> float :
    return 'sum(lista)'

resultTypeHint = testeTypeHint([10, 50, 60])
print(resultTypeHint)



# Função Lambda
# É como uma função anonima utilizada de forma parecida com o perador ternario
media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3)/3

print(media(10, 4, 1))


# A função map
# É uma função que aplica uma determida função a cada elemento de uma estrutura de dados interaveis
def incrementoDeNota (nota) :
    return nota + 0.5 
 
notas = [5, 9, 6]

notasAtualizadas = list(map(incrementoDeNota, notas))

print(notasAtualizadas)
