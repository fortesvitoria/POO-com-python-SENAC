"""
Crie uma função que receba uma lista com vários números e
retorne a soma de todos os números desta lista, o menor número,
o maior número e a média dos valores da lista.
"""
#importa random para selecionar numeros
import random

#cria lista
lista = []

#adiciona numeros aleatórios na lista
for i in range (10):
    numero = random.randint(1,5)
    lista.append(numero)
print(lista)

#cria funcao que recebe os numeros
def soma_lista():
    soma = sum(lista)
    print(f'A soma dos numeros {lista} é {soma}')

#chama função
soma_lista()