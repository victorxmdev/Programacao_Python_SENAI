lista = [10, 20, 30, 40, 50]
try: 
    print(lista[int(input("Indice: "))])
except (ValueError, IndexError): print("Indice inválido ou entrada inválida!")