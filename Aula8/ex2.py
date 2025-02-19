def calc():
    
    print('Cálculo de quadrado: ')

    n1 = int(input('Digite um valor inteiro para descobrir seu quadrado: '))

    try:
        quadrado = n1 ** 2
        print('O quadrado de ', n1, 'é igual a ', quadrado)

    except ValueError:
        print("Erro: entrada inválida")

calc()