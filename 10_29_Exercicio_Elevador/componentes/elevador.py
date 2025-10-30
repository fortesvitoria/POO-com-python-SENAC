# 1 Cria classe elevador
class Elevador:
    # 1.1 Cria construtor, que recebe como parametro um andar
    def __init__(self, andar = 1):
        self.__andar = andar
    
    # 1.2 Cria uma metodo para mover o elevalor, que retorna uma string
    '''
    Metodo locomover(destino) recebe como parametro um destino  e retorna uma string(mensagem)
    ele recebe um destino em formato int que verifica para onde o usuario quer ir
    1. Se o destido for maior ou igual a um e menor ou igual a 15:
        1.1 Se andar for igual a destino, informa que já está no andar
        1.2 Se o destino for igual a um, informa que está indo para o térreo;
        1.3 Senão, informa o andar para o qual está indo.
    2. Se não for menor que um ou maior que 15, retorna mensagem de erro
    '''
    def locomover(self, destino) -> str:
        destino = int(destino)
        if destino >= 1 and destino <= 15:
            if destino == 1 and self.__andar ==1:
                return self.__mensagem_esta_no_terreo()
            elif destino == self.__andar:
                return self.__mensagem_mesmo_andar(destino)
            elif destino == 1 and self.__andar != 1:
                self.__andar = destino
                return self.__mensagem_alteracao_terreo()
            elif destino != self.__andar:
                self.__andar = destino
                return self.__mensagem_alteracao_andar(destino)
        else:
            return self.__mensagem_erro()
    
    # 1.3 Metodo para pegar o andar, retorna um int
    def get_andar(self) -> int:
        return self.__andar
    
    # 1.4 Metodos com mensagens de alerta e de erro, retornam uma string
    def __mensagem_erro(self) -> str:
        return "Andar inválido! Digite um valor entre 1 e 15."
    
    def __mensagem_alteracao_andar(self, andar) -> str:
        return f"Elevador indo para o andar {andar}."
    
    def __mensagem_alteracao_terreo(self) -> str:
        return "Elevador indo para o térreo."
    
    def __mensagem_mesmo_andar(self, andar) -> str:
        return f"Você já está no andar {andar}."
    
    def __mensagem_esta_no_terreo(self) -> str:
        return "Você está no térreo."



