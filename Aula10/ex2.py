def multiplicar_numeros(num1, num2, num3):
    mult = num1 * num2 * num3
    return "O resultado é: ", mult

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
print(multiplicar_numeros(num1, num2, num3))