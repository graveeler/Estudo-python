# operadores lógicos em Python: and , or , not , in ,  < , > , <= , >= , == , != , is , is not , in , not in , any, all
# tipos primitivos de variaveis em python: int, float, str, bool, complex. 
# Outros tipos de variaveis list, tuple, range, dict, set, frozenset entre outros.
# Estruturas condicionais if , else , elif
# Estruturas de repetição while
# python por padrão não permite concatenação de strings com numeros

# ---------------------------- variaveis ----------------------------------

# definição de variaveis
var1 = 10
var2 = 20

# operações com variaveis
result = var1 + var2

print(result)

var1 = input('variavel 1: ') 

var2 = input('variavel 2: ')

print(var1 + var2) # Nesse resultado os valores digitas do input são strings logo ele não somou e sim concatenou

print(f'Resultado é igual a: {result}') # Forma alternativa de concatenação de numeros com strings

print('Resultado é igual a: {}'.format(result)) # Forma alternativa de concatenação valores dentro de uma string


# Python permite criação de variaveis usando acentuação
divisão = 10 / 5

print(divisão)

#  -------------- Exemplo de estruturas Condicionais -----------------------

# OBS python não pussui switch ou cases

# if, else, elif

if var1 < var2:
    print('variavel1 é menor')
elif var1 > var2:
    print('variavel1 é maior')
else :
    print('valores são iguais')

print('teste de concatenacao de strings: ' + 'strings concatenadas com sucesso!')

# Operador ternario
ternario1 = 'variavel1 é maior' if var1 > var2 else 'variavel1 é menor'

print(ternario1)

# OBS 1: pode-se usar uma "\" pra melhorar a legibilidade do código e quebrar uma linha sem afetar seu funcionamento

# OBS 2: No caso do operador ternario a "\" so pode ser usada apos o else, ou seja, so é aceita em partes especificas do código
ternario2 = 'variavel1 é maior' if var1 > var2 else \
'variavel1 é menor' if var1 < var2 else \
'valores são iguais' if var1 == var2 else ''

print(ternario2)

# -------------------------Estruturas de repetição----------------------------------

# while 

# Dentro do for e while tambem podemos usar o os comandos break e continue
whileCont = 1

print('Contagem do While:')

while  whileCont < 10:
    print(f'While cont: {whileCont}')
    whileCont += 1

# for

# OBS 1: O primeiro parametro do range é o valor inicial, o segundo parametro é o valor final -1
# OBS 2: Pode-se tambem ter um terceiro parâmetro que indica o passo, contagem de 1 em 1, 2 em 2...
for i in range(1,11,1) : 
    print(i)


# ---------------------------- Conversão de tipos de dados ---------------------------------






# ---------------------------- Collections ---------------------------------
#o que são modulos e pacotes ?

# Listas 

# OBS 1: Listas so funcionam com indices bem definidos, como numeros inteiros

lista1 = [1,2,3,'teste']

print(lista1, lista1[2])

# Dicionario

# OBS 1: Dicionarios funcionam tanto com indices numericos

dicionario1 = {'chave1':1,"chave2":2, 5:10}

print(dicionario1, dicionario1['chave2'])




#ENUMERATE, STARTWITH()

# --------------------------------------------------------
# -----------------Observações gerais---------------------
# --------------------------------------------------------

# .split = explode  obs: o split sem parametro separa por espaços vazios
# implode ja é tem uma abordagem totalmente diferente, variavel com unificador e join
# len() contar quantidade itens numa lista e caracteres num string
# conceito de partição numa lista é carregar os elementos em um intervalo de indices dentro dela(provavelmente indices numericos, mas existe a possibilidade de ser strings tambem)
# estudar metodos de listas
# pesquisar diferenças entre tupla, lista e dicionario





#--------------------------------------------------------