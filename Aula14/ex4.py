def compara_dez(numero):
    match numero:
        case numero if numero > 10:
            return "Maior que 10"
        case numero if numero < 10:
            return "Menor que 10"
        case 10:
            return "Igual a 10"

print(compara_dez(15))
print(compara_dez(5))
print(compara_dez(10))