class Pessoa:
    def __init__(self, nome, idade): #cria construtor
        self.nome = nome #atributo de instancia
        self.idade = idade #atributo de instancia

    #preciso alterar algum dado, para isso criamos um metodo
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    #metodo para mostrar o nome de forma correta
    def get_nome(self):
        return self.nome

    #metodo para alterar idade
    def set_idade(self, novo_idade):
        self.idade = novo_idade

    #metodo para mostrar a idade
    def get_idade(self):
        return self.idade


p1 = Pessoa('Felipe', 35) #instancia p1
p1.nome = 'Mario' #rescreve o nome, pouca segurança

p2 = Pessoa('Maria', 30) #instancia p2
p2.set_nome('Vitoria') #altera nome atraves do metodo dentro da classe, forma correta
p2.set_idade(34) #altera idade

print(p1, p1.nome,p1.idade) #nao se mostra nome desta forma, se cria um metodo
print(p2, p2.get_nome(), p2.get_idade()) #forma correta de mostrar um nome

