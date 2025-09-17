class Usuario:
    def __init__(self, nome, usuario_id, senha):
        self.__nome = nome
        self.__id = usuario_id
        self.__senha = senha
        self.__locker_reservado = None


class Administrador(Usuario):
    def __init__(self, nome, usuario_id, senha):
        super().__init__(nome, usuario_id, senha)
        self.__is_admin = True

