import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

while True:
    try:
        ano_nascimento = int(input("Digite o ano em que você nasceu: "))
        idade = calcular_idade(ano_nascimento)
        print(f"Esse ano você completou ou irá completar", idade ,"anos.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano ou 'sair'.")