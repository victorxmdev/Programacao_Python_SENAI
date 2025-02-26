def classifica_idade(idade):
    match idade:
        case idade if 0 <= idade < 12:
            return "Criança"
        case idade if 12 <= idade < 18:
            return "Jovem"
        case idade if 18 <= idade < 60:
            return "Adulto"
        case idade if idade >= 60:
            return "Idoso"
        case _:
            return "Idade inválida"

print(classifica_idade(10))
print(classifica_idade(15))
print(classifica_idade(30))
print(classifica_idade(70))
print(classifica_idade(-5))