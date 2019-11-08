while 1:
    inteiro = int(input("Entre com um valor inteiro a ser processado:   "))
    try: 
        print( 1/ inteiro )
        break
    except ZeroDivisionError:
        print("Infinito")
        break
    except ValueError:
        print("Número digitado não é um inteiro, tente novamente.\n")
    except 
        print("Erro inesperado, tente novamente.\n")
        

#ZeroDivisionError
#TypeError

