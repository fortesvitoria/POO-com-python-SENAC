class Locker:
    def __init__(self, locker_id, tamanho):
        self.__id = locker_id
        self.__tamanho = tamanho
        self.__status = "Disponível"
        self.__reservado_por = None
    
    #Converte o objeto Locker para um dicionário
    def to_dict(self):
        return {
            "id": self.__id,
            "tamanho": self.__tamanho,
            "status": self.__status,
            "reservado_por": self.__reservado_por
        }