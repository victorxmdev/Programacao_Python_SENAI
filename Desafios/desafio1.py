produto1 = {"nome": "Camiseta", "preco": 50.00}
produto2 = {"nome": "Calça", "preco": 100.00}
produto3 = {"nome": "Tênis", "preco": 200.00}

print("Bem-vindo ao sistema de e-commerce!")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

print("\nProdutos disponíveis:")
print("1 - Camiseta (R$ 50,00)")
print("2 - Calça (R$ 100,00)")
print("3 - Tênis (R$ 200,00)")

escolha = int(input("\nDigite o número do produto que deseja comprar: "))
quantidade = int(input("Digite a quantidade desejada: "))

if escolha == 1:
    produto_escolhido = produto1
elif escolha == 2:
    produto_escolhido = produto2
elif escolha == 3:
    produto_escolhido = produto3
else:
    print("Opção inválida! Escolha um número entre 1 e 3.")
    exit()

valor_total = produto_escolhido["preco"] * quantidade

print(f"\nResumo da compra:")
print(f"Produto: {produto_escolhido['nome']}")
print(f"Quantidade: {quantidade}")
print(f"Valor unitário: R$ {produto_escolhido['preco']:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")

print("\nOpções de pagamento:")
print("1 - Cartão de crédito")
print("2 - Boleto bancário")
print("3 - PIX")
forma_pagamento = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

if forma_pagamento == 1:
    print("\nPagamento com cartão de crédito selecionado.")
elif forma_pagamento == 2:
    print("\nPagamento com boleto bancário selecionado.")
elif forma_pagamento == 3:
    print("\nPagamento com PIX selecionado.")
else:
    print("Opção de pagamento inválida!")

print(f"\nObrigado por comprar conosco, {nome}!")
print(f"Um e-mail de confirmação será enviado para: {email}")