preco_simples = 100
preco_duplo = 150
preco_luxo = 250

n = int(input("Quantos clientes vc precisa: "))

for i in range(n):
    print("Cadastro do Cliente", i + 1, ":")
    cliente_nome = input("Digite o nome do cliente: ")
    cliente_idade = int(input("Digite a idade do cliente: "))

    print("Escolha o tipo de quarto para o cliente:")
    print("1 - Simples (R$ 100,00 por dia)")
    print("2 - Duplo (R$ 150,00 por dia)")
    print("3 - Luxo (R$ 250,00 por dia)")

    cliente_quarto = int(input("Digite o número correspondente ao quarto: "))

    if not 1 <= cliente_quarto <= 3:
        print("Opção inválida. Será considerado o quarto Simples.")
        cliente_quarto = 1

    cliente_dias = int(input("Quantos dias o cliente ficará no hotel? "))

    if cliente_quarto == 1:
        valor_cliente = preco_simples * cliente_dias
    elif cliente_quarto == 2:
        valor_cliente = preco_duplo * cliente_dias
    else:
        valor_cliente = preco_luxo * cliente_dias

    print("\nResumo das Reservas:")
    print(f"O valor total para {cliente_nome} é R$ {valor_cliente:.2f}")