"""
O que é uma função?
    Em Python, uma função é uma sequência de comandos
    que executa alguma tarefa e que tem um nome.
    A sua principal finalidade é nos ajudar a organizar
    programas em pedaços.

Nome de uma função.

Variáveis de função. Escopo.

"""

# # Escopo
# def minha_primeira_funcao():
#     global x
#     x = 22
#     print("Estou aqui.")
#     print(x)
#
#
#
# # Programa Principal
# x = 10
# minha_primeira_funcao()
# print(x)


# # Argumento
# def minha_segunda_funcao(arg): # arg = "Tio Ivo"
#     print(arg)
#     arg = "UNISENAC"
#     print(arg)
#


# # Retorno
# def minha_terceira_funcao(arg):
#     return arg.replace("i", "I")
#
# def altera_um_char(texto, pos, caracter):
#     txt2 = ''
#     for i, e in enumerate(texto):
#         if i == pos:
#             txt2 += caracter
#         else:
#             txt2 += e
#     return txt2
#
# # ##### programa principal
# nn = minha_terceira_funcao("Tio Ivo")
# txt = "bla blab bla"
#
# txt = altera_um_char(txt, 0, "B")
# print(txt)


# Retorno Multiplo
def minha_quarta_funcao(arg):
    texto = arg.replace("i", "I")
    lista = texto.split()
    texto2 = texto.upper()
    return texto, lista, texto2

# # ##### programa principal

#x, y, z = minha_quarta_funcao("Ivonei da Silva Marques")
print(minha_quarta_funcao("Ivonei da Silva Marques"))

# print(x)
# print(y)
# print(z)

exit()

