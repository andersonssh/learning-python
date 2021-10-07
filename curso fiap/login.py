import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "fiap":
    print("Usuário logado")
else:
    print("Login Negado")