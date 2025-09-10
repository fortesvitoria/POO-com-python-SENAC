'''
Escopo Detalhado do Sistema Locker
------------------------------------------------------
Objetivo do Sistema:
Desenvolver uma aplicação que gerencie o uso de lockers (armários) por usuários cadastrados, permitindo reserva, liberação, controle de acesso e manutenção. O sistema deve ser capaz de diferenciar tipos de lockers, controlar permissões de usuários e administradores, e garantir segurança e rastreabilidade das operações.

Perfis de Usuário:
Usuário Comum
Pode se cadastrar e fazer login
Reservar e liberar lockers disponíveis
Consultar histórico de uso
Administrador
Possui acesso privilegiado
Pode adicionar, remover ou colocar lockers em manutenção
Visualiza todos os usuários e reservas
Gerencia o sistema de forma geral

Componentes Principais
-----------------------------------
'''

#1. Classe Locker (superclasse)
#Atributos: id, tamanho, status, reservadoPor
#Métodos: abrir(), fechar(), reservar(), liberar()
class Locker:
    def __init__(self, id, tamanho, status, reservadoPor):
        self.id = id
        self.tamanho = tamanho
        self.status = status
        self.reservadoPor = reservadoPor

    def abrir(self):
        #....

    def fechar(self):
        #...

    def reservar(self):
        #...

    def liberar(self):
        #...


#2. Subclasses de Locker
#LockerPequeno, LockerMedio, LockerGrande
#Cada uma pode sobrescrever o metodo reservar() com
#regras específicas (ex: tempo máximo, tipo de objeto permitido)

#3. Interface Reservavel
#Métodos: reservar(), liberar()
#Implementada por todas as subclasses de Locker

#4. Classe Usuario
#Atributos: id, nome, senha, lockerReservado
#Métodos: reservarLocker(), liberarLocker()

class Usuario:
    def __init__(self, id, nome, senha, lockerReservado):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.lockerReservado = lockerReservado

    def reservarLocker(self):
        # ....

    def liberarLocker(self):
        # ...




#5. Classe Administrador (herda de Usuario)
#Métodos adicionais: adicionarLocker(), removerLocker(), colocarEmManutencao()

#6. Classe SistemaLocker
#Atributos: listaDeLockers, usuariosRegistrados
#Métodos: registrarUsuario(), login(), listarLockersDisponiveis(), gerenciarReservas()

class SistemaLocker:
    def __init__(self, listaDeLockers, usuariosRegistrados):
        self.listaDeLockers = listaDeLockers
        self.usuariosRegistrados = usuariosRegistrados

    def registrarUsuario(self):
        # ....

    def login(self):
        # ...

    def listarLockersDisponiveis(self):
        # ...

    def gerenciarReservas(self):
        # ...


'''
Funcionalidades do Sistema:
------------------------------------------
Cadastro e autenticação de usuários
Reserva de lockers com controle de tempo
Liberação de lockers
Visualização de status dos lockers
(livre, ocupado, manutenção)
Histórico de uso por usuário
Gerenciamento de lockers (admin)
Interface de login diferenciada para usuários e administradores
Persistência de dados (JSON, SQLite ou arquivos)
Tratamento de exceções (ex: tentativa de reserva duplicada)
Testes unitários com JUnit (opcional)
Interface gráfica (opcional)
'''


