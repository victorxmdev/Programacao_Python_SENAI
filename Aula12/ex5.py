#Exercício 5 - Soma de números pares

def soma_pares(n):
    return sum(i for i in range(2, n + 1, 2))
