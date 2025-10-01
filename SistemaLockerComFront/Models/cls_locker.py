class Locker:
    def __init__(self, locker_id, tamanho):
        self.__id = locker_id
        self.__tamanho = tamanho
        self.__status = "Disponível"
        self.__reservado_por = None
    
    #Converte o objeto Locker para um dicionário
    def para_dicionario(self):
        return {
            "id": self.__id,
            "tamanho": self.__tamanho,
            "status": self.__status,
            "reservado_por": self.__reservado_por
        }
    
    # Adicionamos getters (properties) para acessar os atributos fora da classe
    @property
    def id(self):
        return self.__id
        
    @property
    def tamanho(self):
        return self.__tamanho
        
    @property
    def status(self):
        return self.__status
        
    # Método para reservar o locker
    def reservar(self, usuario_id):
        if self.__status == "Disponível":
            self.__status = "Ocupado"
            self.__reservado_por = usuario_id
            return True # Sucesso
        return False # Falha

    # Método para liberar o locker
    def liberar(self):
        self.__status = "Disponível"
        self.__reservado_por = None

    def para_dicionario(self):
        return {
            "id": self.__id,
            "tamanho": self.__tamanho,
            "status": self.__status,
            "reservado_por": self.__reservado_por
        }