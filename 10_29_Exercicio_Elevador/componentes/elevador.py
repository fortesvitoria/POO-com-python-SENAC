class Locker:
    def __init__(self, andar = 1):
        self.__andar = andar
    
    def locomover(self, destino) -> str:
        destino = int(destino)
        if destino >= 1 and destino <= 15:
            if destino == self.__andar:
                return self.__mensagem_mesmo_andar(destino)
            elif destino == 1 and self.__andar != 1:
                self.__andar = destino
                return self.__mensagem_alteracao_terreo()
            else:
                self.__andar = destino
                return self.__mensagem_alteracao_andar(destino)
        else:
            return self.__mensagem_erro()
    
    def get_andar(self) -> int:
        return self.__andar

    def __mensagem_erro(self) -> str:
        return "Andar inválido! Digite um valor entre 1 e 15."
    
    def __mensagem_alteracao_andar(self, andar) -> str:
        return f"Elevador indo para o andar {andar}."
    
    def __mensagem_alteracao_terreo(self) -> str:
        return "Elevador indo para o térreo."
    
    def __mensagem_mesmo_andar(self, andar) -> str:
        return f"Você já está no andar {andar}."

elevador = Locker()
print(elevador.get_andar())
print(elevador.locomover(4))
print(elevador.get_andar())
print(elevador.locomover(15))

