#classe pessoa
class Pessoa():
    def __init__(self,nome=""):
        self.nome = nome

    def apresentar(self):
        print(f'Olá, eu sou {self.nome}')

#classe amigo rebendo a classe mae pessoa
class Amigo(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.apelido = nome

    def piada(self):
        print('"Piadinha sem graça"')


#istancia pessoa, criando um objeto
p1 = Pessoa('Vitória')
a1 = Amigo('Otávio')

#classe
print(p1.nome)
p1.apresentar()
print('-'*20)

#herança
a1.piada()
a1.apresentar()
print(a1.nome)