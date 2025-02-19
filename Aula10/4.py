usuarios = ["user1", "user2", "user3"]
try:
    print("Usuário no sistema! " if input("Usuário: ") in usuarios else "Usuário não encontrado!")
except: 
    print("Erro ao verificar usuário")