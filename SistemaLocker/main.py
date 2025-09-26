from Core.sistema import *
from Interface.menus import *

def main():
        print("Inicializando Sistema de Lockers...")
        sistema = SistemaLocker() #instancia sistema locker

        print("Sistema inicializado com sucesso!")
        print("\nUsuários padrão disponíveis:")
        print("   Usuário: user01 | Senha: 1234")
        print("   Usuário: user02 | Senha: abcd")
        print("   Admin:   admin01 | Senha: admin123")

        menu_principal(sistema)

# Programa principal
if __name__ == "__main__":
    sistema = SistemaLocker()
    menu_principal(sistema)

