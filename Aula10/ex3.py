def elevar_numeros(num1):
    pot = num1 ** 2
    return "O valor da potência de ", num1, "é igual a ", pot

num1 = int(input("Digite o valor que deseja elevar a 2: "))
print(elevar_numeros(num1))