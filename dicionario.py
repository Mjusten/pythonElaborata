lista = [1,4,"Batman"]


#declarar dicionário
#1
d = dict()
#2 ou
d= {}
#3 populando
d = {"cliente":"Alexandre", "seila":"Batman","texto":12,"outra":True}

arvore = {"a": {
    "Alexandre": 12,
    "André" : 14,
    },
    "b": {
        "Batman": 16,
        "Bruno": 18,
    }
}

cliente = {
    "12": {
        "nome": "Batman",
        "endereco": "Caverna",
        "telefone": [50,51],
    },
    "14": {

    },
}

#Busca

print(d["seila"])
print(arvore["b"]["Batman"])

print(cliente["12"])
print(cliente["12"]["telefone"])
print(cliente["12"]["telefone"][0])

print(d)

#Adição

d["abacate"] = "feira"

chave = input()
valor = input()
d["laranja"] = {chave:valor}


print(d)

#Métodos

print("-"*50)
print(d.keys())
print(d.values())
print("-"*50)
print(cliente.keys())
print(cliente["12"].values())


if "12" in cliente.keys():
    print("YES")

#caracteristicas

cliente["16"] = {} #Cria, pois não existe
cliente["14"] = {} #Substitui, pois já existe

for c in cliente:
    print(c)

for c in cliente.values():
    print(c)
