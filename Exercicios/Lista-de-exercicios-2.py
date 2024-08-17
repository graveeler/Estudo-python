# Exercicios propostos por esse link: http://www2.uesb.br/editora/wp-content/uploads/Exercicios-resolvidos-utilizando-Python-21.08.2023.pdf

# 1. Elaborar um programa Python para somar os digitos de um número menor que 100.
value = 50
result = 0

while value < 100 or value > 0:
    print('pra encerrar o programa digite EXIT')
    value = input('Digite um numero menor que 100: ')
    
    if value == 'EXIT' :
        break
    
    if not value.isdigit() :
        print('valor digitado precisa ser numerico e maior que 0') 
        value = 10
        continue
        
    #value = int(value)
        
    if int(value) > 100 or int(value) < 0:
        print('Digite apenas valores entre 0 e 100!')
        value = 10
        continue
        
   
    for i in range(0,len(value))  :
        result += int(value[i])
        
    print(result)
    
    value = 10
    result = 0
   