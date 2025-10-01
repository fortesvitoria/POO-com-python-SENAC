import json # para manipulação de arquivos JSON
from Models.cls_locker import *
from Models.cls_usuario import *
from pathlib import Path #para reconhecer o caminho do arquivo

class SistemaLocker:
    def __init__(self, arquivo_dados="Data/sistema_dados.json"):
        # Dicionários para armazenar os objetos de usuário e locker em memória, usando o ID como chave 
        self.__usuarios = {} 
        self.__lockers = {} 
        
        # --- LÓGICA PARA TORNAR O CAMINHO ABSOLUTO ---
        # 2. Encontra o caminho do arquivo atual (sistema.py)
        caminho_script = Path(__file__).resolve()
        # 3. Sobe um nível para chegar na pasta raiz do projeto (a pasta que contém 'Core' e 'Data')
        caminho_raiz = caminho_script.parent.parent
        # 4. Monta o caminho completo e seguro para o arquivo de dados
        self.__arquivo_dados = caminho_raiz / arquivo_dados
        # --- FIM DA LÓGICA ---

        self.carregar_dados() #chamando metodo

    #metodos para ler o arquivo JSON e criar objetos na memória
    def carregar_dados(self):
        # Utilizando o bloco 'try...except' para tratar possíveis erros durante a leitura do arquivo.
        try:
            # Abre o arquivo JSON em modo de leitura ("r"). 
            # O "r" é um parâmetro específico e obrigatório da função open() do Python. 
            #As f: pega esse "objeto de arquivo" e o armazena na varivavel f
            with open(self.__arquivo_dados, "r", encoding="utf-8") as f:
                # Carrega o conteúdo do arquivo JSON para a variável 'dados'.
                dados = json.load(f)

                # Percorre cada usuário na lista "usuarios" do JSON.
                for u in dados["usuarios"]:
                    #se o usuario tem a chave "is_admin" e se é verdadeira
                    if u.get("is_admin"):
                        #se for admin, cria uma instancia da classe Adminstrador
                        usuario = Administrador(u["nome"], u["id"], u["senha"])
                    else:
                        # Caso contrário, cria uma instância da classe Usuario.
                        usuario = Usuario(u["nome"], u["id"], u["senha"])

                    # Adiciona o objeto criado ao dicionário de usuários, usando o ID como chave.    
                    self.__usuarios[u["id"]] = usuario

                # Percorre cada usuário na lista "lockers" do JSON.
                for l in dados["lockers"]:
                    #cria instancia da classe Locker
                    locker = Locker(l["id"], l["tamanho"])
                    #*****************IMPLEMENTAR LOGICA
                    if "reservado_por" in l and l["reservado_por"] is not None:
                        pass

                    # Adiciona o objeto ao dicionário de lockers.
                    self.__lockers[l["id"]] = locker
                
        # Se o arquivo JSON não for encontrado, este erro é capturado.
        except FileNotFoundError:
            print(f"Arquivo {self.__arquivo_dados} não encontrado. Será criado um novo ao salvar.")
        # Se o arquivo JSON estiver mal formatado, este erro é capturado.
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {self.__arquivo_dados}. Verifique o formato do JSON.")
    
    #Metodo para salvar dados
    def salvar_dados(self):
        # Cria um dicionário que será a estrutura do arquivo JSON.
        dados_para_salvar = {
            # Usa "list comprehension", que serve como um .append, mas mais compacto, para converter cada objeto Usuario no dicionário __usuarios para um dicionário, usando o metodo "para_dicionario"
            "usuarios": [usuario.para_dicionario() for usuario in self.__usuarios.values()],
            "lockers": [locker.para_dicionario() for locker in self.__lockers.values()]
        }

        # Abre o arquivo JSON em modo de escrita ("w - write"), apagando o conteúdo anterior.
        with open(self.__arquivo_dados, "w", encoding="utf-8") as f:
            # json.dump escreve o dicionário no arquivo
            # indent=4 formata o arquivo para ficar legível
            # ensure_ascii=False garante que acentos (como em 'Vitória') sejam salvos corretamente
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)

    #Método para cadastrar usuario
    def cadastrar_usuario(self, nome, usuario_id, senha):
        #Verifica se o usuario já existe:
        if usuario_id in self.__usuarios:
            print("Erro: Já existe um usuário com este ID.")
            return False
        
        # Cria um novo objeto Usuario
        novo_usuario = Usuario(nome, usuario_id, senha)
        # Adiciona ao dicionário de usuários em memória
        self.__usuarios[usuario_id] = novo_usuario
        # Salva a alteração no arquivo JSON
        self.salvar_dados()
        print("Usuário cadastrado com sucesso!")
        return True
    
    #Método para cadastrar locker
    def cadastrar_locker(self, locker_id, tamanho):
        #verifica se já existe
        if locker_id in self.__lockers:
            print("Erro: Já existe um locker com este ID.")
            return False
        
        #Cria novo locker
        novo_locker = Locker(locker_id, tamanho)
        self.__lockers[locker_id] = novo_locker
        self.salvar_dados()
        print("Locker cadastrado com sucesso!")
        return True

    #Método para login
    def fazer_login(self, login, senha):
        usuario = self.__usuarios.get(login)
        if usuario and usuario.valida_senha(senha):
            return usuario
        return None
    
    # Property para permitir o acesso (somente leitura) à lista de usuários e lockers de fora da classe.
    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def lockers(self):
        return self.__lockers


