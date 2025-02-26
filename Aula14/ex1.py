def par_ou_impar(numero):
    match numero % 2:
        case 0:
            return "Par"
        case 1:
            return "Ímpar"

print(par_ou_impar(10))
print(par_ou_impar(7))