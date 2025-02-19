def exibir_menu():
    print("---- MENU ----")
    print("1. Salada")
    print("2. Macarronada")
    print("3. Sanduíche")
    print("4. Sorvete")

def escolher_prato(opcao):
    if opcao == 1:
        print("Você escolheu Salada.")
    elif opcao == 2:
        print("Você escolheu Macarronada.")
    elif opcao == 3:
        print("Você escolheu Sanduíche.")
    elif opcao == 4:
        print("Você escolheu Sorvete.")
    else:
        print("Opção inválida.")

exibir_menu()
opcao_cliente = int(input("Escolha o número do prato (1-4): "))
escolher_prato(opcao_cliente)
