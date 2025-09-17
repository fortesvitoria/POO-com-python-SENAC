from Core.sistema import *
from Interface.menus import *

def main():
        print("Inicializando Sistema de Lockers...")
        sistema = SistemaLocker()

        print("Sistema inicializado com sucesso!")
        print("\nUsuários padrão disponíveis:")
        print("   Usuário: user01 | Senha: abcd")
        print("   Admin:   admin01 | Senha: 1234")

        menu_principal(sistema)

# Programa principal
if __name__ == "__main__":
    main()


