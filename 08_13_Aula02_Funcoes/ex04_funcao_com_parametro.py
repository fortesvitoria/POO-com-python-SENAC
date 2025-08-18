"""
Crie uma função que retorne uma lista com 10 números inteiros entre
10 e 1000
"""
#importa funcao random
import random

#cria lista vazia
lista=[]

#cria função sem retorno
def cria_lista():
    for i in range(10): #looping até 10
        numero = random.randint (10,1000) #seleciona aleatoriamente um numero de 10 a 1000
        lista.append(numero) #adiciona os numeros na lista
    print(f'Numeros gerados: {lista}') #imprime lista

#chama a função
cria_lista()