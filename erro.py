while 1:
    try:
        teste = int(input("Entre com o valor:  "))
        break
    except ValueError:
        print("Valor inserido não é um número inteiro")
