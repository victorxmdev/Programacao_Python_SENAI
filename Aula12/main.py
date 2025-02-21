from ex1 import aleatorio
from ex2 import tres_aleatorios
from ex3 import aleatorio_range
from ex4 import contagem_regressiva
from ex5 import soma_pares
from ex6 import tabuada
from ex7 import impares_reverso


print("Número aleatório entre 5 e 10:", aleatorio())
print("Três números aleatórios:", tres_aleatorios())
print("Número aleatório entre 10 e 30:", aleatorio_range())

print("\nContagem regressiva:")
contagem_regressiva()

n = int(input("\nDigite um número para soma de pares: "))
print("Soma dos pares até", n, "é:", soma_pares(n))

n = int(input("\nDigite um número para tabuada: "))
tabuada(n)

print("\nNúmeros ímpares de 99 a 1:")
impares_reverso()
