def calc():

    print('Cálculo de divisão: ')

    n1 = int(input('Digite o dividendo: '))
    n2 = int(input('Digite o divisor:'))

    if (n2 == 0):
        print('Divisão por zero!')
    else:
        calculo = n1 / n2
        print('O resultado é: ', calculo)

calc() 

