preco_simples = 100
preco_duplo = 150
preco_luxo = 250

print("Cadastro do Cliente 1:")
cliente1_nome = input("Digite o nome do cliente 1: ")
cliente1_idade = int(input("Digite a idade do cliente 1: "))
print("Escolha o tipo de quarto para o cliente 1:")
print("1 - Simples (R$ 100,00 por dia)")
print("2 - Duplo (R$ 150,00 por dia)")
print("3 - Luxo (R$ 250,00 por dia)")
cliente1_quarto = int(input("Digite o número correspondente ao quarto: "))
cliente1_dias = int(input("Quantos dias o cliente 1 ficará no hotel? "))

print("\nCadastro do Cliente 2:")
cliente2_nome = input("Digite o nome do cliente 2: ")
cliente2_idade = int(input("Digite a idade do cliente 2: "))
print("Escolha o tipo de quarto para o cliente 2:")
print("1 - Simples (R$ 100,00 por dia)")
print("2 - Duplo (R$ 150,00 por dia)")
print("3 - Luxo (R$ 250,00 por dia)")
cliente2_quarto = int(input("Digite o número correspondente ao quarto: "))
cliente2_dias = int(input("Quantos dias o cliente 2 ficará no hotel? "))

print("\nCadastro do Cliente 3:")
cliente3_nome = input("Digite o nome do cliente 3: ")
cliente3_idade = int(input("Digite a idade do cliente 3: "))
print("Escolha o tipo de quarto para o cliente 3:")
print("1 - Simples (R$ 100,00 por dia)")
print("2 - Duplo (R$ 150,00 por dia)")
print("3 - Luxo (R$ 250,00 por dia)")
cliente3_quarto = int(input("Digite o número correspondente ao quarto: "))
cliente3_dias = int(input("Quantos dias o cliente 3 ficará no hotel? "))

if cliente1_quarto == 1:
    valor_cliente1 = preco_simples * cliente1_dias
elif cliente1_quarto == 2:
    valor_cliente1 = preco_duplo * cliente1_dias
else:
    valor_cliente1 = preco_luxo * cliente1_dias

if cliente2_quarto == 1:
    valor_cliente2 = preco_simples * cliente2_dias
elif cliente2_quarto == 2:
    valor_cliente2 = preco_duplo * cliente2_dias
else:
    valor_cliente2 = preco_luxo * cliente2_dias

if cliente3_quarto == 1:
    valor_cliente3 = preco_simples * cliente3_dias
elif cliente3_quarto == 2:
    valor_cliente3 = preco_duplo * cliente3_dias
else:
    valor_cliente3 = preco_luxo * cliente3_dias

print("\nResumo das Reservas:")
print(f"O valor total para {cliente1_nome} é R$ {valor_cliente1:.2f}")
print(f"O valor total para {cliente2_nome} é R$ {valor_cliente2:.2f}")
print(f"O valor total para {cliente3_nome} é R$ {valor_cliente3:.2f}")