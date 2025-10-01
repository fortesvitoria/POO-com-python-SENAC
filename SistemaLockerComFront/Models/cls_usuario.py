class Usuario:
    def __init__(self, nome, usuario_id, senha):
        self.__nome = nome
        self.__id = usuario_id
        self.__senha = senha
        self.__locker_reservado = None
        
    #@property ajuda a manter o encapsulamento, progetendo os dados, assim acessamos o usuario como usario.nome, e não como usuario.get_not(), o que mantem o código mais seguro. Ela também garante a imutabilidade, tornando os atributos somente para leitura, prevenindo modificações.
    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id
    
    # propriedade para sabermos qual locker o usuário reservou
    @property
    def locker_reservado(self):
        return self.__locker_reservado
        
    #Método para verificar se a senha está correta. Retorna True se forem iguais, e False caso contrário.
    def valida_senha(self, senha):
        return self.__senha == senha
    
    # Método para definir qual locker foi reservado pelo usuário
    def definir_locker_reservado(self, locker_id):
        self.__locker_reservado = locker_id
    
    #Método para converter o objeto Usuario para um dicionário.
    def para_dicionario(self):
        return {
            "nome": self.__nome,
            "id": self.__id,
            "senha": self.__senha,
            "locker_reservado": self.__locker_reservado
        }

# A classe Administrador herda da classe Usuario. Herda todas as caracteristicas e possui nova: is_admin, que inicia como true
class Administrador(Usuario):
    def __init__(self, nome, usuario_id, senha):
        super().__init__(nome, usuario_id, senha)
        self.__is_admin = True

#Método para converter o objeto Administrador para um dicionário (sobrescrevendo o da classe pai)
    def para_dicionario(self):
        # Pega o dicionário da classe pai (Usuario)
        dados = super().para_dicionario()
        # Adiciona a chave específica do admin
        dados["is_admin"] = True
        return dados
