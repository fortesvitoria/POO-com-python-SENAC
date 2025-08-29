'''
Exercício parte 1
Crie uma classe Porta com os atributos: altura, largura, cor.
Crie os métodos para pintar, abrir e fechar a porta.

Exercício parte 2
Crie uma classe Fechadura com a propriedade chave (chave será o segredo).
Crie os métodos de chavear e deschavear.

Na classe porta adicione o atributo fechadura. Crie o método instalar_fechadura.
Agora crie os métodos de trancar e destrancar a porta com a chave.

Você deverá conseguir abrir e fechar a porta se esta estiver destrancada.
Você não conseguirá abrir ou fechar a porta se está já estiver previamente trancada.
'''


# Fechadura
class Fechadura:
    # abaixo atributos de instancia, especificos do objeto
    def __init__(self,
                 segredo):  # cria construtor, nao precisa informar os parametros se todos objetos instanciados forem iguais
        self.chave = segredo
        self.chaveada = False  # deschaveado

    def chave_correta(self, chave):  # verifica se a chave está correta
        if chave == self.chave:
            return True
        return False

    # metodo para chavear
    def chavear(self, chave):
        if chave == self.chave:
            self.chaveada = True  # porta chaveada

    # metodo para deschavear
    def deschavear(self, chave):
        if chave == self.chave:
            self.chaveada = False  # dechaveada

    #verifica se esta chaveada, aqui vamos chamar na classe da porta
    def esta_chaveada(self):
        if self.chaveada == True:
            return True
        return False

    def converte(self):
        if self.chaveada:  # se chaveada for true, devolve chaveada, caso contrario devolte deschaveada
            return "CHAVEADA"
        return "DESCHAVEADA"

    def __str__(self):
        return f'Fechadura: {self.converte()}'


# porta
class Porta:
    marca = "Portas SA"  # atributos de classe, todos objetos o terão

    # abaixo atributos de instancia, especificos do objeto
    def __init__(self):  # cria construtor, nao precisa informar os parametros se todos objetos instanciados forem iguais
        self.altura = 220
        self.largura = 90
        self.cor = None
        self.aberta = True  # se true, a porta está aberta
        self.fechadura = None #fechadura não instalada

    # define nova cor
    def pintar(self, nova_cor):
        self.cor = nova_cor

    # metodo para abrir a porta
    def abrir(self):
        if not self.fechadura or not self.fechadura.esta_chaveada():
            self.aberta = True #sem fechadura ou nao esta chaveada - aberta

    # metodo para fechar a porta
    def fechar(self):
        if not self.fechadura or not self.fechadura.esta_chaveada(): #se não esta com fechadura ou não esta chaveada
            self.aberta = False #porta fechada

    # instalar fechadura
    def instalar_fechadura(self, fechadura):
        self.fechadura = fechadura
        self.aberta = True #se fechadura instalada, porta aberta

    # Agora crie os métodos de trancar e destrancar a porta com a chave.
    def trancar(self, chave):
        if self.fechadura and self.fechadura.chave_correta(chave): #se tem fechadura e a chave esta correta,
            self.fechadura.chavear(chave) #tranca com fechadura

    def destrancar(self, chave):
        if self.fechadura and self.fechadura.chave_correta(chave):
            self.fechadura.deschavear(chave) #destranca

    def converte(self):  # Função para exibir outra mensagem ao inves de true ou false. Se for true retorna aberta, caso contrario fechada
        if self.aberta:
            return "ABERTA"
        return "FECHADA"

    def __str__(self):  # utilizado para mascarar o endereço do objeto com uma mascara de string
        return f'''
        - Marca como atributo instancia: {self.marca}
        - Marca como atributo de classe: {Porta.marca}
        
        Altura: {self.altura} - Largura: {self.largura}
        Cor: {self.cor} - Status: {self.converte()}
        Aberta: {self.aberta}
        {self.fechadura}
            
        '''


################################
p1 = Porta() #cria objeto porta
f1 = Fechadura('123') #cria fechadura com chave

p1.pintar('Azul') #pinta de azul
p1.instalar_fechadura(f1) #instala fechadura informando a fechadura desejada
print(f1)
print('*' * 15)
f1.chavear('123')
print(f1)
print(p1)

'''
p1.instalar_fechadura(f1) #unindo dois objetos = agregação
p1.fechar()
p1.trancar('1234')
p1.abrir()
p1.destrancar('1234')

p2 = Porta()
p2.trancar = False
p2.pintar('Vermelha')
p2.marca = "Portinhas SA" #atributo de tempo de excuçao, gruda no objeto quando o codigo roda, esse marca nao tem a ver com a marca de classe

print(p1)
print(p2)
'''
