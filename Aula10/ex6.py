def verificar_campeonato_masculino(ano):
    if 1930 <= ano <= 2022 and (ano - 1930) % 4 == 0:
        return True
    else:
        return False

def verificar_campeao(ano):
    anos_campeonatos = [0]
    if ano in anos_campeonatos:
        return "Estados Unidos nunca foi campeão"
    else:
        return False

ano_usuario = int(input("Digite um ano para verificar se houve Copa do Mundo e se os Estados Unidos foram campeões: "))

if verificar_campeonato_masculino(ano_usuario):
    print(f"Houve Copa do Mundo de Futebol Masculino em {ano_usuario}.")
    print(f"Os Estados Unidos não foram campeões da Copa do Mundo de Futebol Masculino em {ano_usuario}.")
else:
    print(f"Não houve Copa do Mundo de Futebol Masculino em {ano_usuario}.")
