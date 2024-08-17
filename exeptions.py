# --------------------------------- Exceptions --------------------------------------
teste = [1, 2, 3]

# Exception mais basico básico 
try:
    print(teste[2])
except Exception as e:
    print(e)   
    
# Exception utlizando else
try:
    print(f"Linha 12: {teste[2]}")
except Exception as e:
    print(e)   
else:
    print(f"Linha 16:")
    
# Exception utlizando Finally
try:
    print(f"Linha 12: {teste[2]}")
except Exception as e:
    print(e)   
else:
    print(f"Linha 16:")
finally:
    print('tudo encerrado')