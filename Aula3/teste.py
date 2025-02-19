print('Formulario:')

nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite o nome do seu curso: ")
salario = float(input("Digite seu salário: "))
casado = input("Casado(a)? (Sim/Não): ").lower() == 'sim' 

print("---||---")
print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)
print("Salário:", salario)
print("Casado:", casado)