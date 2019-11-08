flag = 0

try: 
    arquivo = open("/home/aluno/Documentos/aulapython/usuarios.txt","r")
except FileNotFoundError:
    print("Arquivo não encontrado")
    flag = 1
except:
    print("Erro Desconhecido")    
    flag = 1

if flag == 0:
    usuarios = arquivo.readlines()
    arquivo.close()

    dados = []
    user = []
    percentual = []

    for usuario in usuarios:
        usuario = usuario.replace("\n","")
        usuario = usuario.split("\t")
        user.append(usuario[0].capitalize())
        dados.append(float((usuario[1]))/(1024*1024))

    for dado in dados:
        #uso = (dado / sum(dados))*100
        #percentual.append(uso)
        percentual.append((dado/sum(dados))*100)

    if len(dados) == len(user) and len(dados) == len(percentual):
        j = len(dados)
        arquivo = open("/home/aluno/Documentos/aulapython/relatorio.txt","w")
        arquivo.write("Empresa INC. \tUso do espaço em disco por usuário\n")
        arquivo.write("--------------------------------------------------\n")
        arquivo.write("Nr. Usuário \tEspaço utilizado \t%do uso\n\n")

        i = 1 
        while i <= j:
            arquivo.write("{}  {}\t{} MB \t\t{}%\n".format(i,user[i-1],round(dados[i-1],2),round(percentual[i-1],2)))
            i = i +1

        arquivo.write("\n\nEspaço total ocupado: {} MB\n".format(round(sum(dados),2)))
        arquivo.write("Espaço médio ocupado: {} MB".format(round((sum(dados)/j),2)))
        arquivo.close()
    else:
        print("Dados incorretos")
else:
    print("Finalizando programa")