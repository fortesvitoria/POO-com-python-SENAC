
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
            login = input("Digite seu login: ").strip()
            senha = input("Digite sua senha: ").strip()
            
            usuario_logado = sistema.fazer_login(login, senha)  
            if usuario_logado:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario_logado.nome}.")
                # Aqui você chamaria o próximo menu, por exemplo, menu_usuario(usuario_logado)
            else:
                print("\nCredenciais inválidas. Tente novamente.")
        elif opcao == "2":
            pass

        elif opcao == "3":
            print("\nEncerrando o sistema.")
            break

        else:
            print("Opção inválida. Digite 1, 2 ou 3.")
