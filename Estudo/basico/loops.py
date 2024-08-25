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



print(range(1,12))

# List Comprehension


# range foi feito pra loops  ou onde mais da pra usa-lo?