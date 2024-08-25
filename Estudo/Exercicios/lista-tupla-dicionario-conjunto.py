print('--------------------------------------------------------------------------------------')
print('-------------------------------- Listas ----------------------------------------------')
print('--------------------------------------------------------------------------------------')

# Lista é uma coleção ordenada e mutavel. Permite membros duplicados
lista = ["carro", True, 5, 6.4]
print(lista)
print(type(lista))
print(lista[3])


print('--------------------------------------------------------------------------------------')
print('-------------------------------- Tuplas ----------------------------------------------')
print('--------------------------------------------------------------------------------------')

# Tupla é uma coleção ordenada e imutavel. Permite membros duplicados(ver o que isso quer dizer ?????)
# É como se fosse um array de valores constantes que não podem ser adicionados ou removidos.
# tupla, com um unico elemento, tem que ser finalizado com virgula, caso contrario é reconhecido como string

tupla = ("carro", True, 5, 6.4)
print(tupla)
print(type(tupla))
print(tupla[0])
veiculo, logica = ("Moto", False) # procurar o nome dessa atribuição
print(veiculo, logica)


print('--------------------------------------------------------------------------------------')
print('------------------------------- Dicionario -------------------------------------------')
print('--------------------------------------------------------------------------------------')

# O dicionario é uma coleção ordenada e mutavel. Nenhum membro duplicado
# ?
dicionario = {"nome" : "carro","Logica": True,"inteiro": 5,"float":  6.4, "testeDuplicacaoValor": 5}
print(dicionario)
print(type(dicionario))
print(dicionario["inteiro"])

#valores do dicionario
print(f"values: {dicionario.values()}")
print(f"chaves: {dicionario.keys()}")


print('--------------------------------------------------------------------------------------')
print('-------------------------------- Conjuntos -------------------------------------------')
print('--------------------------------------------------------------------------------------')

# Set (Conjunto) é uma coleção não ordenada e não indexada, nenhum membro duplicado
# Se houver valores duplicados ele ignora e contabiliza apenas 1 deles
conjunto = {"carro",True, 5, 6.4, 5, 5}
print(conjunto)
print(type(conjunto))
#print(conjunto[1])



print('--------------------------------------------------------------------------------------')
print('-------------------------------- List Comprehension -------------------------------------------')
print('--------------------------------------------------------------------------------------')

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e','f','g','h','i','j']
stringName = 'Paulo da Silva'

# Modo de uso mais basico 
result1 = [item1 if item1 > 5 else 0 for item1 in list1]
print('-------------------------------- RESULT 1 -------------------------------------------')
print(result1)

# Modo de uso do list comprehensiion com condicionais ANTES do for (essa opção suporta o else)
result2 = [item1 if item1 > 5 else 0 for item1 in list1]
print('-------------------------------- RESULT 2 -------------------------------------------')
print(result2)

# Modo de uso do list comprehensiion com condicionais Depois do for (essa opção NÃO suporta o else)
result3 = [item2 for item2 in list2 if item2 == 'a']
print('-------------------------------- RESULT 3 -------------------------------------------')
print(result3)

# Modo de uso do list comprehensiion com condicionais ANTES e DEPOIS do for
result4 = [item2 if item2 != 'b' else 'B' for item2 in list2 if item2 != 'j']
print('-------------------------------- RESULT 4 -------------------------------------------')
print(result4)

# Modo de uso do list comprehensiion com condicionais ANTES e DEPOIS do for, com loops aninhados
result5 = [(item1, item2) if item1 < 5 else (0, item2) for item1 in list1 for item2 in list2 if item2 != 'b']
print('-------------------------------- RESULT 5 -------------------------------------------')
print(result5)

# Obtendo todas as listas
result6 = [x for x in [stringName, list1, list2]]
print('-------------------------------- RESULT 6 -------------------------------------------')
print(result6)

# Usando string como lista
result7 = [(letra) for letra in stringName]
print('-------------------------------- RESULT 7 -------------------------------------------')
print(result7)

# O recurso de python referente ao implode em php, que junta novamente os itens de um array de string é o .join
print(''.join(result7))

# Usando list comprehension pra imprimir uma string de 2 em 2 letras
# Esse operador [indice:indice+2] serve pra pegar uma string de um indice a outro, o resultado vai do indice antes 
# do ":" ate o valor depois [indice Inicial : Indice final], chama-se fatiamento ou slice

result7 = [stringName[indice:indice+2]  for indice in range(0, len(stringName), 2)]

print('-------------------------------- RESULT 6 -------------------------------------------')
print(result7)


