#importando biblioteca para tratar datas
from datetime import date
#definindo o programa valorPagamento
def valorPagamento(prestacao=0,atraso=0):
    if atraso > 0:
        return (prestacao*(1+0.03+(atraso*0.001)))
    elif atraso == 0:
        return (prestacao)
    else:
        print("Atraso não pode ser negativo")
        return 0
#definindo variáveis de apoio para escrever o relatório
SomaPrest = 0
NumPrest = 0
while 1:
    prestacao = float(input("Entre o valor nominal da prestação:    "))
#valor da prestação não pode ser menor que 0
    if prestacao < 0 :
        print("Prestação não pode ser negativa.")
#valor 0 da prestação sai do programa
    elif prestacao == 0:
        print("Saindo do programa.")
        break
#qualquer outro valor vai para o próximo input (dias em atraso)    
    else:
        atraso = int(input("Entre o número de dias em atraso:    "))
#dias não podem ser negativos (porém podem ser 0)        
        if atraso < 0 :
            print("Atraso não pode ser negativo.")
        else:
            atualizado = valorPagamento(prestacao,atraso)
#usando as variáveis de apoio para receberem o valor total pago e a quantidade de prestações que foram pagas no dia
            SomaPrest = SomaPrest + atualizado
            NumPrest = NumPrest + 1
            print("Valor atualizado para pagamento é: {} reais".format(round(atualizado,2)))
data = date.today()
#definindo uma flag para tratar arquivo existente e inexistente
flag = 0
try:
    arquivo = open("C:\\Python\\Exercicios\\relatorio-{}.txt".format(data),"r")
#se o arquivo não existe, cria, fecha e abre como leitura
except FileNotFoundError:
    arquivo = open("C:\\Python\\Exercicios\\relatorio-{}.txt".format(data),"w+")
    #arquivo.close()
    #arquivo = open("C:\\Python\\Exercicios\\relatorio-{}.txt".format(data),"r")    
#porém cria uma flag = 1 para mostrar que o arquivo está "em branco"    
    flag = 1
except:
    print("erro desconhecido")
#le o conteudo do arquivo (se estiver em branco, lê "")
conteudo = arquivo.readlines()
#usando a flag 1 para arquivos em branco, faz um append do cabeçalho (1º data, 2º descrição)
if flag == 1:
    conteudo.append("Relatório de {}\n".format(date.today()))
    conteudo.append("Valor\tnº de prestações pagas\n")
#para todo o resto é igual, faz um append das variáveis de apoio do programa
conteudo.append("{} \t {} \n".format(round(SomaPrest,2),NumPrest))
#escreve o conteudo no arquivo e fecha
arquivo = open("C:\\Python\\Exercicios\\relatorio-{}.txt".format(data),"w")
arquivo.writelines(conteudo)
arquivo.close()