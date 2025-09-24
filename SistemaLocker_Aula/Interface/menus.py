
def exibir_cabecalho(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo.center(56)}")
    print("=" * 60)



def menu_principal(sistema):
    while True:
        exibir_cabecalho("SISTEMA DE LOCKERS - BEM-VINDO")

        print("\nEscolha uma opção:")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

        opcao = input("\nDigite sua opção (1-3): ").strip()

        if opcao == "1":
            pass

        elif opcao == "2":
            pass

        elif opcao == "3":
            print("\nEncerrando o sistema.")
            break

        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


