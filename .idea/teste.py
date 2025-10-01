# Importa a biblioteca 'json' para manipulação de arquivos JSON.
import json
# Importa as classes Locker e Usuario de seus respectivos arquivos.
from Models.cls_locker import *
from Models.cls_usuario import *
# Importa a classe 'Path' da biblioteca 'pathlib' para lidar com caminhos de arquivo de forma robusta.
from pathlib import Path

# Classe principal que orquestra todas as operações do sistema.
class SistemaLocker:
    # O método construtor. 'arquivo_dados' tem um valor padrão.
    def __init__(self, arquivo_dados="Data/sistema_dados.json"):
        # Dicionários para armazenar os objetos de usuário e locker em memória,
        # usando o ID como chave para acesso rápido.
        self.__usuarios = {} 
        self.__lockers = {} 
        
        # --- LÓGICA PARA TORNAR O CAMINHO DO ARQUIVO INDEPENDENTE DO LOCAL DE EXECUÇÃO ---
        # 1. Pega o caminho completo do arquivo atual (sistema.py).
        caminho_script = Path(__file__).resolve()
        # 2. Navega "para cima" duas vezes na estrutura de pastas para chegar à raiz do projeto.
        caminho_raiz = caminho_script.parent.parent
        # 3. Constrói o caminho completo para o arquivo JSON.
        self.__arquivo_dados = caminho_raiz / arquivo_dados
        # --- FIM DA LÓGICA ---

        # Chama o método para carregar os dados do JSON assim que o sistema é inicializado.
        self.carregar_dados()

    # Método para ler os dados do arquivo JSON e criar os objetos em memória.
    def carregar_dados(self):
        # O bloco 'try...except' trata possíveis erros durante a leitura do arquivo.
        try:
            # Abre o arquivo JSON em modo de leitura ("r").
            with open(self.__arquivo_dados, "r", encoding="utf-8") as f:
                # Carrega o conteúdo do arquivo JSON para a variável 'dados'.
                dados = json.load(f)

                # Itera sobre cada dicionário de usuário na lista "usuarios" do JSON.
                for u in dados["usuarios"]:
                    # Verifica se o usuário tem a chave "is_admin" e se ela é verdadeira.
                    if u.get("is_admin"):
                        # Se for admin, cria uma instância da classe Administrador.
                        usuario = Administrador(u["nome"], u["id"], u["senha"])
                    else:
                        # Caso contrário, cria uma instância da classe Usuario.
                        usuario = Usuario(u["nome"], u["id"], u["senha"])
                    # Adiciona o objeto criado ao dicionário de usuários, usando o ID como chave.
                    self.__usuarios[u["id"]] = usuario

                # Itera sobre cada dicionário de locker na lista "lockers" do JSON.
                for l in dados["lockers"]:
                    # Cria uma instância da classe Locker.
                    locker = Locker(l["id"], l["tamanho"])
                    # (A lógica de reserva ainda não está totalmente implementada aqui).
                    if "reservado_por" in l and l["reservado_por"] is not None:
                        pass
                    # Adiciona o objeto ao dicionário de lockers.
                    self.__lockers[l["id"]] = locker
                
                # Mensagem de depuração para confirmar que os dados foram carregados.
                print(f"DEBUG: Dados carregados com sucesso! IDs dos usuários: {list(self.__usuarios.keys())}")

        # Se o arquivo JSON não for encontrado, este erro é capturado.
        except FileNotFoundError:
            print(f"Arquivo {self.__arquivo_dados} não encontrado. Será criado um novo ao salvar.")
        # Se o arquivo JSON estiver mal formatado, este erro é capturado.
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {self.__arquivo_dados}. Verifique o formato do JSON.")

    
    # Método para salvar os dados atuais (dos dicionários em memória) de volta para o arquivo JSON.
    def salvar_dados(self):
        # Cria um dicionário que será a estrutura do arquivo JSON.
        dados_para_salvar = {
            # Usa "list comprehension" para converter cada objeto Usuario no dicionário __usuarios para um dicionário (usando o método to_dict).
            "usuarios": [usuario.to_dict() for usuario in self.__usuarios.values()],
            # Faz o mesmo para os objetos Locker.
            "lockers": [locker.to_dict() for locker in self.__lockers.values()]
        }

        # Abre o arquivo JSON em modo de escrita ("w"), apagando o conteúdo anterior.
        with open(self.__arquivo_dados, "w", encoding="utf-8") as f:
            # Usa json.dump para escrever o dicionário no arquivo.
            # indent=4 formata o JSON para ser legível por humanos.
            # ensure_ascii=False permite que caracteres especiais (acentos) sejam salvos corretamente.
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)

    # Método para adicionar um novo usuário ao sistema.
    def cadastrar_usuario(self, nome, usuario_id, senha):
        # Verifica se o ID do novo usuário já existe no dicionário de usuários.
        if usuario_id in self.__usuarios:
            print("Erro: Já existe um usuário com este ID.")
            return False  # Retorna False para indicar que o cadastro falhou.
        
        # Cria um novo objeto da classe Usuario.
        novo_usuario = Usuario(nome, usuario_id, senha)
        # Adiciona o novo usuário ao dicionário em memória.
        self.__usuarios[usuario_id] = novo_usuario
        # Chama o método para salvar as alterações no arquivo JSON.
        self.salvar_dados()
        print("Usuário cadastrado com sucesso!")
        return True # Retorna True para indicar sucesso.
    
    # Método para adicionar um novo locker ao sistema.
    def cadastrar_locker(self, locker_id, tamanho):
        # Verifica se o ID do locker já existe.
        if locker_id in self.__lockers:
            print("Erro: Já existe um locker com este ID.")
            return False
        
        # Cria um novo objeto Locker.
        novo_locker = Locker(locker_id, tamanho)
        # Adiciona o novo locker ao dicionário em memória.
        self.__lockers[locker_id] = novo_locker
        # Salva as alterações no arquivo.
        self.salvar_dados()
        print("Locker cadastrado com sucesso!")
        return True

    # Método para autenticar um usuário.
    def fazer_login(self, login, senha):
        # O método .get(login) busca pelo login no dicionário __usuarios.
        # Se não encontrar, retorna None, evitando um erro.
        usuario = self.__usuarios.get(login)
        # Verifica duas coisas: 
        # 1. Se um usuário foi encontrado (usuario is not None)
        # 2. Se a senha fornecida é válida (chamando o método do próprio objeto Usuario).
        if usuario and usuario.valida_senha(senha):
            return usuario  # Retorna o objeto do usuário logado.
        return None  # Retorna None se o login falhar.
    
    # Property para permitir o acesso (somente leitura) à lista de usuários de fora da classe.
    @property
    def usuarios(self):
        return self.__usuarios

    # Property para permitir o acesso (somente leitura) à lista de lockers.
    @property
    def lockers(self):
        return self.__lockers