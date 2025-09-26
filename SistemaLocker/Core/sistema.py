import json
from Models.cls_locker import *
from Models.cls_usuario import *
from pathlib import Path #para reconhecer o caminho do arquivo

class SistemaLocker:
    def __init__(self, arquivo_dados="Data/sistema_dados.json"):
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


    def carregar_dados(self):
        try:
            with open(self.__arquivo_dados, "r", encoding="utf-8") as f:
                dados = json.load(f)

                for u in dados["usuarios"]:
                    if u.get("is_admin"):
                        usuario = Administrador(u["nome"], u["id"], u["senha"])
                    else:
                        usuario = Usuario(u["nome"], u["id"], u["senha"])
                    self.__usuarios[u["id"]] = usuario

                for l in dados["lockers"]:
                    locker = Locker(l["id"], l["tamanho"])
                    if "reservado_por" in l and l["reservado_por"] is not None:
                        pass
                    self.__lockers[l["id"]] = locker
                
                # ADICIONE ESTA LINHA PARA VER O QUE FOI CARREGADO
                print(f"DEBUG: Dados carregados com sucesso! IDs dos usuários: {list(self.__usuarios.keys())}")

        except FileNotFoundError:
            print(f"Arquivo {self.__arquivo_dados} não encontrado. Será criado um novo ao salvar.")
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {self.__arquivo_dados}. Verifique o formato do JSON.")

    
    #Metodo para salvar dados
    def salvar_dados(self):
        dados_para_salvar = {
            "usuarios": [usuario.to_dict() for usuario in self.__usuarios.values()],
            "lockers": [locker.to_dict() for locker in self.__lockers.values()]
        }

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
    
    #@property ajuda a manter o encapsulamento, progetendo os dados, assim acessamos o usuario como usario.nome, e não como usuario.get_not(), o que mantem o código mais seguro. Ela também garante a imutabilidade, tornando os atributos somente para leitura, prevenindo modificações.
    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def lockers(self):
        return self.__lockers


