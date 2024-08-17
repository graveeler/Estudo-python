import os
import pprint

caminho ='D:\Jogos\PC\Lineage\Freya'
procura = 'Freya' 

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos: 
        pprint.pprint(arquivo)