while 1:
    quantidade_turmas = int(input("Entre o número de turmas:  "))

    if quantidade_turmas >0:
        break

i = 0
quantidade_alunos = 0
while i < quantidade_turmas:
    quantidade_alunos_porTurma = int(input("Entre o número de alunos da %dª turma:   "%(i+1)))
    if quantidade_alunos_porTurma <= 40 and quantidade_alunos_porTurma > 0:
        quantidade_alunos = quantidade_alunos + quantidade_alunos_porTurma
        i = i+1
    else:
        print("Número de alunos incorreto. Repita.")

media = quantidade_alunos / quantidade_turmas
print("A média de alunos por turma é de {}".format(media))