import os

# Exercício 1: Criar e ler um Arquivo
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Conteúdo de exemplo')

with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)