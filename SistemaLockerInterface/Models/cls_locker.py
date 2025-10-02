class Locker:
    def __init__(self, locker_id, tamanho):
        self.__id = locker_id
        self.__tamanho = tamanho
        self.__status = "Disponível" # Pode ser: Disponível, Ocupado, Manutenção
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
    
    @property
    def reservado_por(self):
        return self.__reservado_por
        
    # Método para reservar o locker
    def reservar(self, usuario_id):
        if self.__status == "Disponível":
            self.__status = "Ocupado"
            self.__reservado_por = usuario_id
            return True # Sucesso
        return False 

    # Método para liberar o locker
    def liberar(self):
        self.__status = "Disponível"
        self.__reservado_por = None

    # Método para definir o status para manutenção
    def definir_status(self, novo_status):
    # Validação simples para os status permitidos
        if novo_status in ["Disponível", "Ocupado", "Manutenção"]:
            self.__status = novo_status
            # Garante que um locker em manutenção ou disponível não tenha um dono
            if novo_status != "Ocupado":
                self.__reservado_por = None
            return True
        return False

    def para_dicionario(self):
        return {
            "id": self.__id,
            "tamanho": self.__tamanho,
            "status": self.__status,
            "reservado_por": self.__reservado_por
        }