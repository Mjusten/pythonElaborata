class Cliente:
    #Construtor
    def __init__(self,nome,cpf,endereco,telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def verificaCpf(self):
        pass
    
    def cadastra(self):
        pass

c = Cliente("Batman",15,"Gotham City",10)
print(c.nome,c.cpf,c.endereco,c.telefone)
