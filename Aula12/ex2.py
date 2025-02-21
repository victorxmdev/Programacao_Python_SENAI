#Exercício 2 - Criar 3 números aleatórios

import random

def tres_aleatorios():
    return [random.randint(1, 100) for _ in range(3)]
