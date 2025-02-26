def string_vazia(texto):
    match texto:
        case "":
            return "Vazia"
        case _:
            return "Não vazia"

print(string_vazia("Olá"))
print(string_vazia(""))