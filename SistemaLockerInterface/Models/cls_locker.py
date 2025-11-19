from datetime import datetime, timedelta

class Locker:
    def __init__(self, locker_id, tamanho):
        self.__id = locker_id
        self.__tamanho = tamanho
        self.__status = "Disponível" # Pode ser: Disponível, Ocupado, Manutenção
        self.__reservado_por = None
        self.__data_reserva = None
        self.__tempo_maximo_timedelta = None
    
    # SERIALIZAÇÃO: Método para converter o objeto Locker para um dicionário (converte em JSON).
    def para_dicionario(self):
        return {
            "id": self.__id,
            "tamanho": self.__tamanho,
            "status": self.__status,
            "reservado_por": self.__reservado_por,
            "data_reserva": self.__data_reserva.isoformat() if self.__data_reserva else None
        }
    
    #ENCAPSULAMENTO: Adicionamos getters (properties) para acessar os atributos fora da classe
    @property
    def id(self):
        return self.__id
        
    @property
    def tamanho(self):
        return self.__tamanho
        
    @property
    def status(self):
        return self.__status
    
    @property
    def reservado_por(self):
        return self.__reservado_por
    
    @property
    def data_reserva(self):
        if self.__data_reserva:
            return self.__data_reserva.strftime('%d/%m/%Y %H:%M:%S')
        return None
    
    # ABSTRAÇÃO: Esconde a complexidade do cálculo de datas do resto do sistema.
    # Saida: String formatada ou "Expirado" ou None
    @property
    def tempo_restante(self):
        if self.__status != "Ocupado" or not self.__data_reserva or not self.__tempo_maximo_timedelta:
            return None
        
        data_limite = self.__data_reserva + self.__tempo_maximo_timedelta

        restante = data_limite - datetime.now()

        if restante.total_seconds() <= 0:
            return "Expirado" #saida
        
        # Formata o tempo restante para (HH:MM:SS)
        # str(restante) vem como "HH:MM:SS.microseconds"
        return str(restante).split('.')[0] #saida
        
    # Método para reservar o locker
    def reservar(self, usuario_id):
        if self.__status == "Disponível":
            self.__status = "Ocupado"
            self.__reservado_por = usuario_id
            self.__data_reserva = datetime.now()

            # Define o tempo máximo da reserva
            if self.__tamanho == 'P':
                self.__tempo_maximo_timedelta = timedelta(hours=1)
            elif self.__tamanho == 'M':
                self.__tempo_maximo_timedelta = timedelta(hours=2)
            elif self.__tamanho == 'G':
                self.__tempo_maximo_timedelta = timedelta(hours=4)
            else:
                self.__tempo_maximo_timedelta = timedelta(hours=1)

            return True # Sucesso
        return False 

    # Método para liberar o locker
    def liberar(self):
        self.__status = "Disponível"
        self.__reservado_por = None
        self.__data_reserva = None # Limpa a data
        self.__tempo_maximo_timedelta = None # Limpa o tempo

    # Método para definir o status para manutenção
    def definir_status(self, novo_status):
    # Validação simples para os status permitidos
        if novo_status in ["Disponível", "Ocupado", "Manutenção"]:
            self.__status = novo_status
            # Garante que um locker em manutenção ou disponível não tenha um dono
            if novo_status != "Ocupado":
                self.__reservado_por = None
                self.__data_reserva = None
                self.__tempo_maximo_timedelta = None
            return True
        return False

    def definir_data_reserva_e_limite_ao_carregar(self, data_reserva_obj):
       # Usado pelo sistema.py ao carregar dados do JSON 
        self.__data_reserva = data_reserva_obj
        # Define o tempo máximo (necessário para calcular o tempo restante)
        if self.__tamanho == 'P':
            self.__tempo_maximo_timedelta = timedelta(hours=1)
        elif self.__tamanho == 'M':
            self.__tempo_maximo_timedelta = timedelta(hours=2)
        elif self.__tamanho == 'G':
            self.__tempo_maximo_timedelta = timedelta(hours=4)
        else:
            self.__tempo_maximo_timedelta = timedelta(hours=1)