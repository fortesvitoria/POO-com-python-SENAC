from Core.sistema import *
from Interface.menus import *

def main():
        print("Inicializando Sistema de Lockers...")
        sistema = SistemaLocker() #cria uma instancia sistema locker, que gerencia toda logica do programa

        print("Sistema inicializado com sucesso!")
        print("\nUsuários padrão disponíveis:")
        print("   Usuário: user01 | Senha: 1234")
        print("   Usuário: user02 | Senha: abcd")
        print("   Admin:   admin01 | Senha: admin123")

        #chama o menu principal no documento menus.py e passa a instância do sistema como argumento, 
        # para que o menu possa interagir com os dados e métodos do sistema.
        menu_principal(sistema)

# Programa principal
if __name__ == "__main__":
    main()
