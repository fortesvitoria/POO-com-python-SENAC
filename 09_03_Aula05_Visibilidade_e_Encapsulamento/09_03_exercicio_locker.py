#https://www.winnsen.com/
# inspiração:  https://www.google.com/search?q=lockers&rlz=1C5CHFA_enBR837BR837&oq=&gs_lcrp=EgZjaHJvbWUqCQgBECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyDwgCEC4YJxjHARjqAhjRAzIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkyOTQ3ajBqMTWoAgiwAgHxBXRxFddWa1PS&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:7c0a56c5,vid:m98zvUA61a8,st:0

# Você deverá criar um sistema de locker de entrega de produtos.
# Lógica: O entregador realiza a entrega de um produto escolhendo a opção ENTREGA.
#               Informa o tamanho do pacote, o apartamento e finaliza a entrega. O sistema envia uma mensagem ao nome do apartamento cadastrado com uma senha gerada aleatóriamente.
#
#.             O morador, ao retirar o produto, informa o apartamento e a senha, o locker "Abre". O morador Finaliza a retirada e o locker é liberado.
#
#.             Em configurações deve existir uma opção de cadastro, onde o usuário irá cadastrar o apartamento e uma senha para utilizar o locker.

"""
Sistema de Locker

1- Entrega
    Pequeno, Médio, Grande
    Apartamento
    Finalizar a entrega
    Enviar mensagem de encomenda Disponível com senha(aleatória) para liberar o locker.

2- Retirar Pedido
    Apartamento
    SenhaCadastrada+Senha_Gerada

3- Configurações
    Cadastrar Morador
        Apartamento, Senha
----
Armario - sistema de locker - produto pronto ou configuravel:
- Quantidade (quantos total e quantos de cada)

Usuário:

Apartamentos:

Locker:
- Capacidade: P/M/G
- Identificação: int
- Senha
-


"""

