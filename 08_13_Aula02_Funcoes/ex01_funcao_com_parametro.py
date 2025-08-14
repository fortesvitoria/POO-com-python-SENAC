"""
Crie uma função que retorne quantos caracteres há em uma string
"""

def conta_caractere(palavra):
    quantidade = 0
    for i in range(len(palavra)):
        quantidade += 1
    print(f'Existem {quantidade} letras em {palavra}')


conta_caractere('Vitoria')