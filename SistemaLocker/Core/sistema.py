
from Models.cls_locker import *
from Models.cls_usuario import *

class SistemaLocker:
    def __init__(self, arquivo_dados="Data/sistema_dados.json"):
        self.__usuarios = {}
        self.__lockers = {}
        self.__arquivo_dados = arquivo_dados
        self.__inicializar_dados_padrao()


    def __inicializar_dados_padrao(self):
        admin = Administrador("Ivonei", "admin01", "1234")
        user = Usuario("Carlos", "user01", "abcd")

        self.__usuarios["admin01"] = admin
        self.__usuarios["user01"] = user

        self.__lockers[101] = Locker(100, "Pequeno")
        self.__lockers[102] = Locker(100, "Medio")
        self.__lockers[103] = Locker(100, "Grande")


    def carregar_dados(self):
        pass
    
    def fazer_login(self, login, senha):
        usuario = self.__usuarios.get(login)
        if usuario and usuario.valida_senha(senha):
            return usuario
        return None


