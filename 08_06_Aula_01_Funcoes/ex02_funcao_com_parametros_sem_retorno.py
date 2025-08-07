#2- Crie uma função que
# 1. receba como parâmetro um número_inicial e um número_final, e
# 2. mostre todos os números inteiros no intervalo entre número_inicial e número_final.

#Cria função com dois parametros e sem retorno
def mostra_numeros(num_inicial,num_final):
    #para i in range num_inical+1, para mostrar a partir do 15 e até o 54
    for i in range (num_inicial + 1,num_final):
        print(i)

#Chama função com parametros
mostra_numeros(15,55)