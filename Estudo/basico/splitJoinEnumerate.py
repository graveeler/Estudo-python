# Split Serve dividir uma string por um delimitador especificado por parametro, por padrão é ' '
frase1 = "Essa é a primeira frase"

split1 = frase1.split(' ')

print(split1)


# join serve pra unir itens de uma lista
join1 = ' '.join(split1)

print(join1)

# Enumerate, aplica indices numericos numa lista (interaveis) OBS: cria uma lista de tuplas

for indice, valor in enumerate(split1) :
    print(indice, valor)


enumerate1 = list(enumerate(split1))

print(enumerate1)








