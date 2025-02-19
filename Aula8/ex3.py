def calc():
    
    print('Calcular multipliação: ')

    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor:'))

    try:
        calculo = n1 * n2
        print('O resultado é: ', calculo)

    except ValueError:
        print("Erro: entrada inválida")

calc()