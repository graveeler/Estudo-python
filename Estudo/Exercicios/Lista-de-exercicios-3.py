# Exercicios



#Criando listas de listas
notasDosAlunosJunto = ['joao', 5.5, 3.5, 10, 'maria', 7.5, 6, 9, 'pedro', 5.5, 8.0, 4.0 ]

alunos = []
notas = []
todasAsNotas =[]

for i in range(len(notasDosAlunosJunto)): 

    if i % 4 == 0:
        alunos.append(notasDosAlunosJunto[i])
    else:
        notas.append(notasDosAlunosJunto[i])
        

for i in range(0, len(notas),3) :
    todasAsNotas.append([notas[i], notas[i+1], notas[i+2]])
    
      
print('--------------------Lista de listas-------------------------\n')        
print(alunos, todasAsNotas)        
print('------------------------------------------------------------\n')  

#Criando listas de Dicionarios
notasDosAlunosJunto = ['joao', 5.5, 3.5, 10, 'maria', 7.5, 6, 9, 'pedro', 5.5, 8.0, 4.0 ]

notasDosAlunosSeparados = []

for aluno in range(0, len(notasDosAlunosJunto),4):
    notasDosAlunosSeparados.append({"Nome": notasDosAlunosJunto[aluno], \
                                    "nota1": notasDosAlunosJunto[aluno + 1], 
                                    "nota2": notasDosAlunosJunto[aluno + 2], 
                                    "nota3": notasDosAlunosJunto[aluno + 3], 
                               })
    
print('--------------------Lista de Dicionarios-------------------------\n')       
print(notasDosAlunosSeparados)
print('------------------------------------------------------------\n')  


# utilize uma variavel cujo o valor seja uma string com 10 caracteres e imprima na tela de 2 em 2 caracteres. exemplo:
# varString = 'João Silva' e seja impresso 'Jo', 'ão', ' S', 'il', 'va'

