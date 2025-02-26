def positivo_negativo_zero(numero):
    match numero:
        case numero if numero > 0:
            return "Positivo"
        case numero if numero < 0:
            return "Negativo"
        case 0:
            return "Zero"

print(positivo_negativo_zero(5))
print(positivo_negativo_zero(-3))
print(positivo_negativo_zero(0))