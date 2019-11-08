nomes = []
notas1 = []
notas2 = []
notas3 = []
medias = []
nome = 0
i = 1

while nome != "":
    nome = input("Digite o nome do aluno:  ")
    if nome != "":    
        nomes.append(nome) 
        nota1 = float(input("Digite a primeira nota do aluno:  "))
        nota2 = float(input("Digite a segunda nota do aluno:  "))
        nota3 = float(input("Digite a terceira nota do aluno:  "))
        media = (nota1 + nota2 + nota3)/3
        notas1.append(nota1)
        notas2.append(nota2)
        notas3.append(nota3)
        medias.append(media)
        i = i +1
    else:
        break

j = 1

for nome,nota1,nota2,nota3,media in nomes,notas1,notas2,notas3,media:
    print(nomes)
    print(notas1)
    print(notas2)
    print(notas3)
    print(medias)
