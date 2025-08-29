class Porta:
    def __init__(self):
        self.altura = 220
        self.largura = 90
        self.cor = None
        self.aberta = True
        self.fechadura = None

    def instalar_fechadura(self, fechadura):
        self.fechadura = fechadura
        self.aberta = True

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def trancar(self, chave):
        if self.fechadura and self.fechadura.chave_correta(chave):
            self.fechadura.chavear(chave)

    def destrancar(self, chave):
        if self.fechadura and self.fechadura.chave_correta(chave):
            self.fechadura.deschavear(chave)

    def abrir(self):
        if not self.fechadura or not self.fechadura.esta_chaveada():
            self.aberta = True

    def fechar(self):
        if not self.fechadura or not self.fechadura.esta_chaveada():
            self.aberta = False

    def converte(self):
        if self.aberta:
            return "ABERTA"
        return "FECHADA"

    def __str__(self):
        return f"""
        Altura: {self.altura}  Largura: {self.largura}
        cor: {self.cor}  Status: {self.converte()}  
        {self.fechadura} """

class Fechadura:
    def __init__(self, segredo):
        self.chave = segredo
        self.chaveada = False

    def chave_correta(self, chave):
        if chave == self.chave:
            return True
        return False

    def chavear(self, chave):
        if chave == self.chave:
            self.chaveada = True

    def deschavear(self, chave):
        if chave == self.chave:
            self.chaveada = False

    def esta_chaveada(self):
        if self.chaveada:
            return True
        return False

    def converte(self):
        if self.chaveada:
            return "CHAVEADA"
        return "DESCHAVEADA"

    def __str__(self):
        return f"Fechadura: {self.converte()}"


p1 = Porta()
f1 = Fechadura("1234")

p1.instalar_fechadura(f1)

p1.fechar()
p1.trancar("1234")
p1.destrancar("1234")
p1.abrir()
p1.trancar("1234")
p1.fechar()

print(p1)

