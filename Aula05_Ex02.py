name_user = 0
password = 0

while name_user == password:
    name_user = input("Entre o nome do usuário:   ")
    password = input("Digite a senha:   ")
    if name_user == password:
        print("Senha não pode ser igual ao nome do usuário, por favor, tente novamente:")

print("Login efetuado com sucesso")