#  -------------- Exemplo de estruturas Condicionais -----------------------
# Estruturas condicionais if , else , elif

# OBS python não pussui switch ou cases

# if, else, elif

if 10 < 20:
    print('valor 1 é menor')
elif 10 > 20:
    print('valor 1 é maior')
else :
    print('valores são iguais')

print('teste de concatenacao de strings: ' + 'strings concatenadas com sucesso!')

# Operador ternario
ternario1 = 'variavel1 é maior' if 20 > 10 else 'variavel1 é menor'

print(ternario1)

# OBS 1: pode-se usar uma "\" pra melhorar a legibilidade do código e quebrar uma linha sem afetar seu funcionamento

# OBS 2: No caso do operador ternario a "\" so pode ser usada apos o else, ou seja, so é aceita em partes especificas do código
ternario2 = 'variavel1 é maior' if 40 > 30 else \
'variavel1 é menor' if 10 < 30 else \
'valores são iguais' if 10 == 30 else ''

print(ternario2)




