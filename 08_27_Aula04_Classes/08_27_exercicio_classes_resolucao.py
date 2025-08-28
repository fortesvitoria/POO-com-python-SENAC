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

class Porta:
    marca = "Portas SA" #atributos de classe, todos objetos o terão
    #abaixo atributos de instancia, especificos do objeto
    def __init__(self, largura=60): #cria construtor, nao precisa informar os parametros se todos objetos instanciados forem iguais
        self.modelo = "A001"
        self.altura = 220
        self.largura = largura
        self.cor = None
        self.aberta = True #se true, a porta está aberta

    #define nova cor
    def pintar(self, nova_cor):
        self.cor = nova_cor

    #metodo para abrir a porta
    def abrir(self):
        self.aberta = True

    #metodo para fechar a porta
    def fechar(self):
        self.aberta = False

    def converte(self): #Função para exibir outra mensagem ao inves de true ou false. Se for true retorna aberta, caso contrario fechada
        if self.aberta:
            return "ABERTA"
        return "FECHADA"

    def __str__(self): #utilizado para mascarar o endereço do abjeto com uma mascara de string
        return f'''
        - Marca como atributo instancia: {self.marca}
        - Marca como atributo de classe: {Porta.marca}
        
        Altura: {self.altura} - Largura: {self.largura}
        Cor: {self.cor} - Status: {self.converte()}
    
        '''

################################
p1 = Porta(90)
p1.pintar('Azul')
p1.fechar()
p2 = Porta()
p2.pintar('Vermelha')
p2.marca = "Portinhas SA" #atributo de tempo de excuçao, gruda no objeto quando o codigo roda, esse marca nao tem a ver com a marca de classe

print(p1)
print(p2)
