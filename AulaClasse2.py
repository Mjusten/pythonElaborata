class Usuario:
    def __init__(self,id,nome,espaco):
        self.nome = nome
        self.id = id
        self.espaco = espaco

    def percentual(self):
        return self.espaco * 100 / total 
        

entrada = open("usuarios.txt", "r")
usuarios = entrada.readlines()
lista = []
total = 0.0
i=0

for chave, user in enumerate(usuarios):

    user = user.replace("\n", "").split("\t")
    a = int(chave) + 1
    c = ((float(user.pop()))/(1024 * 1024))
    b = (user.pop())
    total = total + c
    lista.append(Usuario(a,b,c))
    i = i +1

saida = open("relatorio.txt", "w")
saida.write("""Empresa Inc.\tUso do espaço em disco por usuário \n""")
saida.write("-"*50 + "\n")	
saida.write("""Nr.\tUsuário\tEspaço Utilizado\t% do uso\n\n""")
j = 0

while j != i:
    saida.write(str(lista[j].id) + "\t" + str(lista[j].nome) + "    \t" + str(round(float(lista[j].espaco),2)) + "    l \t" + str(round(lista[j].percentual(),2)) +"%\n")
    j = j +1


saida.write("""Espaço total ocupado: {}\n""".format(total))
saida.write("""Espaço médio ocupado: {}""".format(total/i))
entrada.close()
saida.close()