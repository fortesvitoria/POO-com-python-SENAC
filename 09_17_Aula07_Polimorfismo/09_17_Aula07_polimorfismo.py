#SOBBRECARGA - variso metodos com mesmo nome, porém com assinaturas diferentes
def metodo_um(self): #Assinatura do metodo, é a primeira linha
    pass

def metodo_um(self,parametro1): #Assinatura do metodo, é a primeira linha
    pass

def metodo_um(self,parametro1,parametro2 = 'padrao'): #Assinatura do metodo, é a primeira linha
    pass

#Em algumas linguens posso ter todos metodos com o mesmo nome, porém a assinatura é diferente - sobrecarga.
#Porem python nao tem sobrecarga, ele acaba executando somente o ultimo metodo

#Solução sobrecarga:
#recebo varios numeros - chamado de overload
def somar(*nums):
    return sum(nums)

print(somar(1,2,3))

#SOBRESCRITA - mesmo metodo em diferentes classes
class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Latindo"

class Gato(Animal):
    def emitir_som(self):
        return "Miando"

class Cavalo(Animal):
    def emitir_som(self):
        return "Relinchando"

lista_animais = [Cachorro(), Gato(), Cavalo()]
for animal in lista_animais:
    print(animal.emitir_som())
