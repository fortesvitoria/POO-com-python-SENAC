from componentes.elevador import *

def main():
        elevador = Elevador() #cria uma instancia 
        print(elevador.get_andar())
        print(elevador.locomover(4))
        print(elevador.get_andar())
        print(elevador.locomover(15))

# Programa principal
if __name__ == "__main__":
    main()
