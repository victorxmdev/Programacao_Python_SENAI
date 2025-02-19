try:
    a, b = float(input("Número 1: ")), float(input("Número 2: "))
    print(a / b if b != 0 else "Divisão por zero!")
except ValueError: print ("Entrada Inválida")