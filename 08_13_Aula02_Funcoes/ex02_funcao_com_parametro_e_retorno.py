"""
Crie uma função que receba um número inteiro como parâmentro e
retorne quantos dígitos há neste número

"""

def recebe_num(numero): #recebe um numero inteiro
    return len(str(numero)) #converte para string para contar os digitos e retorna o valor

print(recebe_num(100))