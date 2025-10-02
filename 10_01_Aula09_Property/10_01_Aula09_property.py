'''@property é um decorador, uma 'máscara' que ajuda a manter o encapsulamento, progetendo os dados, assim acessamos o usuario 
como usario.nome, e não como usuario.get_nome(), o que mantem o código mais seguro. Ela também garante a imutabilidade, 
tornando os atributos somente para leitura, prevenindo modificações.

- Usado para dar aos metodos de uma uma classe a aparencia de atributos.
- Permite usá-los como atributo, sem os ()
- Property sempre está associado ao método get

ao inves de:
        ti.set_nome("Ana")
        print(ti.get_nome())

fica:

    dentro da classe:
        nome = property(get_nome, set_nome)

    fora:
        ti.nome = "Ana"
        print(ti)

    ou decorando os metodos:
        def nome(self): //getter
            return self.__nome
        
        @nome.setter //setter
        def nome(self,nome):
            self.__nome = nome
'''
class Pessoa:
    def __init__(self,nome, idade, endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

    @property #decorado property
    def endereco(self): #get_endereco
        return self.__endereco

    @endereco.setter #decorado property
    def endereco(self,novo_endereco):
        self.__endereco = novo_endereco

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

p = Pessoa("Vitoria", 34, "Rua das Flores 77")
# p.set_nome("Vitor")
print(p.get_nome())
p.endereco = "Rua das estrelas 45"
p.idade = 33
print(p.idade)
print(p.endereco)