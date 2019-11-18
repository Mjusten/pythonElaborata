
cliente = {}

decisao = 0
while decisao == 0:
    while 1:
        print("Cadastro de novo usuário:\n")
        cpf = input("Digite o CPF do usuário:  ")
        if cpf in cliente.keys():
            print("Cliente já cadastrado")
            break
        else:
            nome = input("Digite o nome do usuário:  ")
            telefone = input("Digite o telefone do usuário:  ")
        cliente = { "cpf" : cpf ,  "nome" : nome , "telefone" : telefone  }
        while 1:
            decisao = input("Deseja cadastrar o próximo usuário? S/N   ")
            if decisao == "S":
                decisao = 0
                break
            elif decisao == "N":
                decisao = 1
                break
            else:
                print("Valor não reconhecido")
        break
    
for c in cliente.values():
    print(c)