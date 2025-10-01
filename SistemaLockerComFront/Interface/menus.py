# Função de utilidade para imprimir um cabeçalho formatado no console
def exibir_cabecalho(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo.center(56)}")
    print("=" * 60)


#menu usuario logado
def menu_usuario_logado(sistema, usuario):
    while True:
        exibir_cabecalho(f"ÁREA DO USUÁRIO - Olá, {usuario.nome}!")
        print("1. Reservar um Locker")
        print("2. Ver meu locker reservado")
        print("3. Voltar ao menu principal")
        
        opcao = input("\nDigite sua opção (1-3): ").strip()

        if opcao == "1":
            # Mostra os lockers disponíveis para o usuário
            print("\n--- Lockers Disponíveis ---")
            disponiveis = False
            for locker in sistema.lockers.values():
                if locker.status == "Disponível":
                    print(f"  ID: {locker.id} | Tamanho: {locker.tamanho}")
                    disponiveis = True
            
            if not disponiveis:
                print("Nenhum locker disponível no momento.")
                continue

            locker_id = input("Digite o ID do locker que deseja reservar: ").strip().upper()
            # Chama o método do sistema para fazer a reserva
            sistema.reservar_locker(usuario, locker_id)

        elif opcao == "2":
            if usuario.locker_reservado:
                print(f"\nVocê tem o locker '{usuario.locker_reservado}' reservado.")
            else:
                print("\nVocê não possui nenhum locker reservado.")
        
        elif opcao == "3":
            print("\nFazendo logout...")
            break # Quebra o loop e volta para o menu principal
        
        else:
            print("Opção inválida. Tente novamente.")


#menu de cadastro para usuario:
def menu_cadastro(sistema):
    exibir_cabecalho("MENU DE CADASTRO PARA USUÁRIO")
    
    nome = input("Digite o nome do novo usuário: ").strip()
    # Loop para garantir que o ID não seja vazio
    while True:
        # Solicita o nome do novo usuário e remove espaços em branco extras do início e do fim com a funcao .strip().
        novo_id = input("Digite o ID (login) para o novo usuário: ").strip()
        if novo_id: #se não estiver vazio, quebra e continua com o programa
            break
        print("O ID não pode ser vazio. Tente novamente.") #se estiver vazio, pede para entrar com um usuário
    
    # Loop para garantir que a senha não seja vazia
    while True:
        senha = input("Digite a senha para o novo usuário: ").strip()
        if senha:
            break
        print("A senha não pode ser vazia. Tente novamente.")

    # Chama o método de cadastro do objeto sistema
    sistema.cadastrar_usuario(nome, novo_id, senha)

# Define o menu principal da aplicação.
def menu_principal(sistema):
    while True:
        exibir_cabecalho("SISTEMA DE LOCKERS - BEM-VINDO")

        print("\nEscolha uma opção:")
        print("1. Login")
        print("2. Cadastro de usuário")
        print("3. Sair")

        opcao = input("\nDigite sua opção (1-3): ").strip()

        # Se a opção for "1", executa a lógica de login.
        if opcao == "1":  
            login = input("Digite seu login: ").strip()
            senha = input("Digite sua senha: ").strip()

            #chama o método fazer_login do objeto sistema.
            usuario_logado = sistema.fazer_login(login, senha)  
            #se conseguiu logar, aparece mensafem de bem vindo, junto com nome do usuário
            if usuario_logado:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario_logado.nome}.")
                # Se o login for sucesso, chama o novo menu de usuário
                menu_usuario_logado(sistema, usuario_logado)
            else:#senao, aparece mensagem pedindo para tentar novamente
                print("\nCredenciais inválidas. Tente novamente.")

        # Se a opção for "2", chama o menu de cadastro do usuario.
        elif opcao == "2":
            menu_cadastro(sistema)

        # Se a opção for "3", encerra o programa.
        elif opcao == "3":
            print("\nEncerrando o sistema.")
            break
        # Se o usuário digitar qualquer outra coisa.
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")
