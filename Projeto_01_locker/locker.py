import usuario

class Locker:
    def __init__(self, id, tamanho, status, reservado_por):
        self.id = id
        self.tamanho = tamanho
        self.status = status
        self.reservado_por = reservado_por
        self.aberta = False
        self.trancada = True

    def abrir(self,id):
        if self.trancada == True and self.aberta == False and id == self.id:
            self.aberta = True
            self.trancada = False
            print('Aberta.')
        else:
            print('Trancada')

    def fechar(self, id):
        if self.trancada == False and self.aberta == True and id == self.id:
            self.aberta = False
            self.trancada = True
            print('Fechada e Trancada')
        else:
            print('Aberta')


    #def reservar(self):
        #...

    #def liberar(self):
        #...
#

l1 = Locker('123', 'M', 'Reservado', 'Mario')
l1.abrir('123')
l1.fechar('123')