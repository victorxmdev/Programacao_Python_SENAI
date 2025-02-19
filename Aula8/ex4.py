def calc():
    
    lista = input("Digite os elementos da lista separados por espaço: ").split()

    try:
        indice = int(input("Digite o índice do elemento que deseja acessar: "))
        print(lista[indice])
    except IndexError:
        print("Erro: Índice fora dos limites")
    except ValueError:
        print("Erro: Entrada inválida")

calc()