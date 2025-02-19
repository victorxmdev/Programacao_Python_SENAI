def maioridade(idade):
    if idade == 18:
        return "Parabéns, você acabou de fazer 18 anos"
    elif idade < 18:
        return "Volte para casa, você ainda é menor de idade"
    else:
        return "Você já é maior de idade faz um tempo"
    
idade = int(input("Quantos anos você tem: (Digite em numerais) "))
print(maioridade(idade))
15