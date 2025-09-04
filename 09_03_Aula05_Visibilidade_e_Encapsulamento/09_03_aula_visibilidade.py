'''
Atributos de clase, instancia e de tempo de execução
visibilidade publica, restrita, privada
 dois underlines metodos especiais
um underline - atributo restrito, serve somente como um alerta, nao deve ser acessado diretamente, somente se estritamente necessario
dois underlines - atributo privado - acessiveis somente dentro da classe
restrita - visivel para dentro do do pacote, sabemos que temos que ter cuidado, mas podemos alterá-lo

Encapsulamento é o conceito e a visibilidade é o que torna o conceito possivel

Publica:
self.nome = Vitoria

alterando atraves de atributo de tempo de execução:
pessoa.nome = Marta

Restrita:
self._nome = nome

alterando atraves de atributo de tempo de execução:
pessoa._nome = Marta

Privada não se altera através do atributo de tempo de execução
self.__nome = nome

alterando somente através do metodo set
pessoa.set_nome(Marta)

'''

class Funcionario:
    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = 2500

    def get_nome(self):
        return self.__nome

    def get_cargo(self):
        return self.__cargo

    def get_salario(self):
        return self.__salario


    def set_salario(self, novo_salario):
        self.__salario = novo_salario


f = Funcionario('Ana', 'secretária')
f.set_salario(6000)
print(f'''
    Nome: {f.get_nome()} 
    Cargo: {f.get_cargo()}
    Salário: {f.get_salario()}
''')