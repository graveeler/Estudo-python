"""
Exercicio de projeto com recursos python

- Crie um projeto onde possamos criar registros de varios funcionarios, setores, e salarios e possamos vizualizar qualquer informação tanto geral como especica de cada uma delas.

* crie um dicionario de dados com a lista de usuarios com id, nome e o salario.
* crie uma lista com os cargos de cada funcionario.
* crie funções auxiliares que sirvam pra calcular a média de salario dos funcionarios, qual o funcionario com salario mais alto e mais baixo.


* Crie um app com um menu com varias opções onde possamos ver:
	- Lista de funcionarios.
	- Os funcionarios com os 3 maiores salarios.
	- A media de salarios de todos os funcionarios.
	- A media de salarios de todos os funcionarios de uma determinada função.
	-  
	
* Crie uma biblioteca de erros especifica pra o seu app

* Pra forçar seus conhecimentos nesse projeto usará todo o conhecimento basico na liguagem pyton, variaveis, estruturas de repetição, condicionais, orientação a objeto (encapsulamento, herança, polimorfismo, criação degetters e setters, funções lambidas, operadores ternários
"""



#----------------------------------------------------------------------------------
#------------------------------------- Resolução ----------------------------------
#----------------------------------------------------------------------------------

# R = Criando Dicionario de funcionarios

import statistics

funcionarios = [
	{
		"nome" : "João",
		"id": 1,
		"salario" : 1500
	},
	{
		"nome" : "Maria",
		"id": 2,
		"salario" : 3000
	},

	{
		"nome" : "Paulo",
		"id": 3,
		"salario" : 1200
	},

	{
		"nome" : "José",
		"id": 4,
		"salario" : 4300
	},

	{
		"nome" : "Mateus",
		"id": 5,
		"salario" : 2000
	},

	{
		"nome" : "Lucas",
		"id": 6,
		"salario" : 1500
	}

]
teste2 = 0
teste = [teste2 for funcionario in funcionarios[0]]
print(teste)
exit()
cargos = [
	"Vendedor",
	"SubGerente",
	"Faxineiro",
	"Gerente",
	"Estoquista",
	"Vendedor"
]

option = 0

while option != 5 :

    print("Escolha a opção desejada:\n")
    print("Digite 1: Pra ver a lista de funcionarios")
    print("Digite 2: Pra ver a media salarial ")
    print("Digite 3: Pra ver os 3 funcionarios com maiores salarios ")
    print("Digite 4: Pra ver a media salarial de todos os funcionarios ")
    print("Digite 5: Pra sair \n")
    print("---------------------------------------\n")
    
    option = input("Digite a opção escolhida: ")
    
    if(not option.isdigit()) :
        print("\ninformação invalida! Por favor digite um numero inteiro")
        continue
    
    option = int(option)

    if(option == 1):
        print("\nLista de funcionarios:\n")
        
        for funcionario in funcionarios :
            print(f"ID: {funcionario["id"]}")
            print(f"Nome: {funcionario["nome"]}")
            print(f"Salario: R$ {funcionario["salario"]},00")
            print("-----------------------------------------")
        print()
    if(option == 2):
        salarios = 0
        print(f"Media Salarial da empresa: {statistics.mean([salarios for funcionario in funcionarios] )}")
    
    