
def exibir_cabecalho(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo.center(56)}")
    print("=" * 60)


#menu de cadastro:
def menu_cadastro(sistema):
    exibir_cabecalho("MENU DE CADASTRO")
    
    nome = input("Digite o nome do novo usuário: ").strip()
    # Loop para garantir que o ID não seja vazio
    while True:
        novo_id = input("Digite o ID (login) para o novo usuário: ").strip()
        if novo_id:
            break
        print("O ID não pode ser vazio. Tente novamente.")
    
    # Loop para garantir que a senha não seja vazia
    while True:
        senha = input("Digite a senha para o novo usuário: ").strip()
        if senha:
            break
        print("A senha não pode ser vazia. Tente novamente.")

    # Chama o método de cadastro do sistema
    sistema.cadastrar_usuario(nome, novo_id, senha)


def menu_principal(sistema):
    while True:
        exibir_cabecalho("SISTEMA DE LOCKERS - BEM-VINDO")

        print("\nEscolha uma opção:")
        print("1. Login")
        print("2. Cadastro de usuário")
        print("3. Sair")

        opcao = input("\nDigite sua opção (1-3): ").strip()

        if opcao == "1":  
            login = input("Digite seu login: ").strip()
            senha = input("Digite sua senha: ").strip()
            
            usuario_logado = sistema.fazer_login(login, senha)  
            if usuario_logado:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario_logado.nome}.")
            else:
                print("\nCredenciais inválidas. Tente novamente.")
        elif opcao == "2":
            menu_cadastro(sistema)

        elif opcao == "3":
            print("\nEncerrando o sistema.")
            break

        else:
            print("Opção inválida. Digite 1, 2 ou 3.")
