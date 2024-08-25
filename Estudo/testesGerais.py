# Testando atribuição de valores por valor ou por referencia em variaveis com tipos primitivos
teste = 20
teste2 = teste
teste = 10
print(teste2)

# Testando atribuição de valores por valor ou por referencia copm listas
teste = [1, 2, 3]
teste2 = teste
teste.append(4)
print(teste2)

testeString = 'Meu nome é Neto'
#testeString[2] = 'o'
print(testeString)

lista = ['joao', 'maria', 'pedro']

n1, n2, *outra_lista = lista

print(n1)

# testando operador ternario

ternario = 'é maior' if 10 < 8 else 'é menor'

print(ternario)

#testando funcoes lambdas

funLambda =  lambda x, y : x + y

print(funLambda(10, 5))








