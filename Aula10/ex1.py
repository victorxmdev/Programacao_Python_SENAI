def comparar_numeros(num1, num2):
    if num1 % 2 == num2 % 2 == 0:
        return "Ambos os números são pares."
    elif num1 % 2 == num2 % 2 == 1:
        return "Ambos os números são ímpares."
    elif num1 % 2 == 0:
        return "O primeiro número é par e o segundo é ímpar."
    else:
        return "O primeiro número é ímpar e o segundo é par."

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(comparar_numeros(num1, num2))