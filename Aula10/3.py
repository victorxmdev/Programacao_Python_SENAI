try:
    a = int(input("Digite um número inteiro para transformar em real: "))
    print("O número ",a,"em real fica ",float(a))
except ValueError: print("Entrada não é um número inteiro")