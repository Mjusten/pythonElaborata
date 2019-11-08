while 1:
    try:
        inteiro = int(input("Entre com um valor a ser processado:   "))
    except ValueError:
        print("Valor inválido, tente novamente com valor inteiro.")
        i = 0
    else:
        try: 
            resultado = 1 / inteiro
        except ZeroDivisionError:
            print("Resultado Infinito")
            break
        else:
            print("Resultado = {}".format(resultado))
            break

#ZeroDivisionError
#TypeError

m