import json 
from Models.cls_locker import *
from Models.cls_usuario import *
from pathlib import Path 
from datetime import datetime

class SistemaLocker:
    def __init__(self, arquivo_dados="Data/sistema_dados.json"):
        # COMPOSIÇÃO: O Sistema possui dicionários de usuários e lockers.
        # Os dicionários armazenam os objetos de usuário e locker em memória, usando o ID como chave 
        self.__usuarios = {} 
        self.__lockers = {} 
        
        # Lógica para encontrar o caminho absoluto do arquivo de dados
        # 2. Encontra o caminho do arquivo atual (sistema.py)
        caminho_script = Path(__file__).resolve()
        # 3. Sobe um nível para chegar na pasta raiz do projeto (a pasta que contém 'Core' e 'Data')
        caminho_raiz = caminho_script.parent.parent
        # 4. Monta o caminho completo e seguro para o arquivo de dados
        self.__arquivo_dados = caminho_raiz / arquivo_dados
       

        self.carregar_dados() #chamando metodo

    # metodos para ler o arquivo JSON e criar objetos na memória
    def carregar_dados(self):
        try:
            with open(self.__arquivo_dados, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for u in dados["usuarios"]:
                if u.get("is_admin"):
                    usuario = Administrador(u["nome"], u["id"], u["senha"])
                else:
                    usuario = Usuario(u["nome"], u["id"], u["senha"])

                # Verificamos se o usuário tem um 'locker_reservado' no arquivo JSON.
                # O método .get() é usado para evitar erros caso a chave não exista.
                if u.get("locker_reservado"):
                    # Se tiver, chamamos o método para definir a reserva no objeto do usuário.
                    usuario.definir_locker_reservado(u["locker_reservado"])

                self.__usuarios[u["id"]] = usuario

            for l in dados["lockers"]:
                locker = Locker(l["id"], l["tamanho"])
                if l.get("status") == "Ocupado" and l.get("reservado_por"):
                    locker.reservar(l["reservado_por"])
                    if l.get("data_reserva"):
                        try:
                            # Converte a string ISO do JSON para um objeto datetime
                            data_reserva_obj = datetime.fromisoformat(l["data_reserva"])
                            locker.definir_data_reserva_e_limite_ao_carregar(data_reserva_obj)
                        except (ValueError, TypeError):
                            # Ignora se a data estiver mal formatada ou for nula
                            pass
                elif l.get("status") == "Manutenção":
                    locker.definir_status("Manutenção")
                self.__lockers[l["id"]] = locker

        except FileNotFoundError:
            print(f"Arquivo {self.__arquivo_dados} não encontrado. Será criado um novo ao salvar.")
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {self.__arquivo_dados}. Verifique o formato do JSON.")
    
 
    #Metodo para salvar dados
    def salvar_dados(self):
        # SERIALIZAÇÃO 
        # Cria um dicionário que será a estrutura do arquivo JSON.
        dados_para_salvar = {
            # Usa "list comprehension", que serve como um .append, mas mais compacto, para converter cada objeto Usuario para um dicionário, usando o metodo "para_dicionario"
            "usuarios": [usuario.para_dicionario() for usuario in self.__usuarios.values()],
            "lockers": [locker.para_dicionario() for locker in self.__lockers.values()]
        }
        # PERSISTÊNCIA - salva o arrquivo json em memoria
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
    
    #Método para login
    def fazer_login(self, login, senha):
        usuario = self.__usuarios.get(login)
        if usuario and usuario.valida_senha(senha):
            return usuario
        return None
    
    #Método para reservar locker
    def reservar_locker(self, usuario, locker_id):
        # 1. Verifica se o usuário já tem uma reserva
        if usuario.locker_reservado is not None:
            print(f"Erro: Você já possui um locker reservado ({usuario.locker_reservado}).")
            return False

        # 2. Verifica se o locker_id escolhido existe
        locker = self.__lockers.get(locker_id)
        if not locker:
            print("Erro: O ID do locker informado não existe.")
            return False
        
        # 3. Verifica se o locker está disponível
        if locker.status != "Disponível":
            print(f"Erro: O Locker {locker_id} já está ocupado.")
            return False

        # 4. Reserva o locker
        if locker.reservar(usuario.id):
            usuario.definir_locker_reservado(locker.id)
            self.salvar_dados()
            print(f"Locker {locker_id} reservado com sucesso para {usuario.nome}!")
            return True

        print(f"Erro: Não foi possível reservar o locker {locker_id}.")
        return False
    
     #Funções de usuário
    def liberar_locker(self, usuario):
        locker_id = usuario.locker_reservado
        if not locker_id:
            print("\nVocê não possui nenhum locker reservado para liberar.")
            return False

        locker = self.__lockers.get(locker_id)
        if locker:
            locker.liberar()
            usuario.liberar_locker_reservado()
            self.salvar_dados()
            print(f"\nLocker {locker_id} liberado com sucesso!")
            return True
        else:
            print(f"\nErro de inconsistência: O locker {locker_id} não foi encontrado.")
            usuario.liberar_locker_reservado()
            self.salvar_dados()
            return False

    #Funções de administrador
    def adicionar_locker(self, locker_id, tamanho):
        if not locker_id or not tamanho:
            print("\nErro: ID e Tamanho não podem ser vazios.")
            return False
        if locker_id in self.__lockers:
            print("\nErro: Já existe um locker com este ID.")
            return False
        
        tamanhos_validos = ["P", "M", "G"]
        if tamanho.upper() not in tamanhos_validos:
            print(f"\nErro: Tamanho '{tamanho}' inválido. Use: {', '.join(tamanhos_validos)}")
            return False
        
        novo_locker = Locker(locker_id, tamanho.upper())
        self.__lockers[locker_id] = novo_locker
        self.salvar_dados()
        print(f"\nLocker {locker_id} adicionado com sucesso!")
        return True

    def remover_locker(self, locker_id):
        locker = self.__lockers.get(locker_id)
        if not locker:
            print("\nErro: Locker não encontrado.")
            return False
        
        if locker.status == "Ocupado":
            print(f"\nErro: Locker {locker_id} está ocupado e não pode ser removido.")
            return False

        del self.__lockers[locker_id]
        self.salvar_dados()
        print(f"\nLocker {locker_id} removido com sucesso!")
        return True

    def colocar_em_manutencao(self, locker_id):
        locker = self.__lockers.get(locker_id)
        if not locker:
            print("\nErro: Locker não encontrado.")
            return False

        if locker.status == "Ocupado":
            print(f"\nErro: Não é possível colocar um locker ocupado em manutenção.")
            return False
        
        if locker.definir_status("Manutenção"):
            self.salvar_dados()
            print(f"\nLocker {locker_id} agora está em Manutenção.")
            return True
        return False
    
    def tirar_de_manutencao(self, locker_id):
        # 1. Busca o locker pelo ID fornecido
        locker = self.__lockers.get(locker_id)
        
        # 2. Valida se o locker realmente existe
        if not locker:
            print("\nErro: Locker não encontrado.")
            return False

        # 3. Valida se o locker está em manutenção
        if locker.status != "Manutenção":
            print(f"\nErro: O Locker {locker_id} não está em manutenção.")
            return False

        # 4. Se tudo estiver correto, altera o status para "Disponível"
        #    O método definir_status já existe na classe Locker.
        if locker.definir_status("Disponível"):
            self.salvar_dados() # Salva a alteração no arquivo JSON
            print(f"\nLocker {locker_id} agora está Disponível.")
            return True
        
        return False
    
    # Property para permitir o acesso (somente leitura) à lista de usuários e lockers de fora da classe.
    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def lockers(self):
        return self.__lockers


