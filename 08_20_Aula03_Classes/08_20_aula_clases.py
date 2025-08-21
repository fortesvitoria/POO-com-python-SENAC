class Lampada:
    def __init__(self, modelo, data_fabricacao, status): #cria construtor, inicializando desligada
        self.modelo = modelo #atributo de instancia
        self.data_fabricacao = data_fabricacao #atributo de instancia
        self.status = status

    def ligar(self):
        self.status = True

    def desligar(self):
        self.status = False

    def validar(self):
        if self.status:
            return 'Ligada'
        return 'Desligada' #nao há necessidade do else nesse caso

    def visualizar(self):
        return f'Lampada: {self.validar()}' #retorna a string

def mostrar_status_lampadas(lampadas):
        for i, lampada in enumerate(lampadas = 1):
            print(f'Lampada {i}: {lampada.visualizar(i)}')

    def __str__(self): #quando declaro este metodo dentro da classe para mascarar o endereço da instancia classe
        return 'Mascarando o endereço da classe' #retorna a string, posso usar esse metodo ao inves do visualizar.

#TAREFA:criar 4 lampadas, o codigo decide qual liga e qual desliga, as lampadas estarao dentro de uma lista

lampadas = []

l1 = Lampada('V10', '07/07/2025', False) #instancia l1
print(l1.visualizar())
print(l1)

def menu():
    #lampadas = [Lampada(),Lampada(),Lampada(),Lampada()]
    lampadas = [Lampada() for _ in range(4)] #instanciando lampadas com metodo range dentro da lista, pode ser _ ou qualquer outro nome

    while True:
        mostrar_status_lampadas(lampadas)
        try:
            escolha = int(input('Escolha uma lampada (1 a 4) ou 0 para sair: '))
            if escolha == 0:
                print('Encerrando...')
                break
            if escolha








'''
    #cria função/metodo liga/desliga e verifica status com metodos get/set
    def set_status(self, novo_status):
        self.status = novo_status

    def get_status(self):
        return self.status

print(l1, l1.modelo,l1.data_fabricacao, l1.status) #nao se mostra modelo desta forma, se cria um metodo
print(l1.get_status())


l1.set_status(True) #altera status com metodo set
print(l1.get_status())
'''

#l1.status = True #mexendo diretamente no atributo, não recomendável
#print(f'Status: {l1.status} - ligada. Desligando: {l1.desligar()}')



