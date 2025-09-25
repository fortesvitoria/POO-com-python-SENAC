class Usuario:
    def __init__(self, nome, usuario_id, senha):
        self.__nome = nome
        self.__id = usuario_id
        self.__senha = senha
        self.__locker_reservado = None
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def login(self):
        return self.__login
        
    def valida_senha(self, senha):
        return self.__senha == senha


class Administrador(Usuario):
    def __init__(self, nome, usuario_id, senha):
        super().__init__(nome, usuario_id, senha)
        self.__is_admin = True

