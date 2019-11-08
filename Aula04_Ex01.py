salario_atual = float(input("Entre o valor do salário atual do colaborador:    "))
erro = 0
if salario_atual >0 and salario_atual <= 1280:
	aumento = 20
elif salario_atual > 1280 and salario_atual <= 1700:
	aumento = 15
elif salario_atual >1700 and salario_atual <=2500:
	aumento = 10
elif salario_atual >2500: 
	aumento = 5
else:
	erro = 1
	print("Valor digitado está incorreto!")

if erro == 0: 
	salario_novo = ((aumento/100)+1)*salario_atual
	# print ("Salário Atual é de {} reais".format(salario_atual))
	# print ("O aumento a ser aplicado é de {}%".format(aumento))
	# print ("O aumento então é de {} reais".format(salario_novo-salario_atual))
	# print ("Assim, o salário novo é de {} reais".format(salario_novo))
	print ("Salário Atual é de {} reais \nO percentual de aumento a ser aplicado é de {}% \nO aumento então então é de {} \nAssim, o salário novo é de {} reais".format(salario_atual,aumento,salario_novo-salario_atual,salario_novo)  )

