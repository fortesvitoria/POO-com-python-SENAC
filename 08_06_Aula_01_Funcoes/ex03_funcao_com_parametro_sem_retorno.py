# 3- Crie uma função que
# 1. receba como parâmetro uma frase e
# 2. retorne a quantidade de caracteres desta string.
# 3. Imprima esta quantidade.

##### EXEMPLO 01
#cria função com parametro
def mostra_frase(frase):
    #usa o len para contar o numero de caracteres da frase e imprime
    print(f' A quantidade de  caracteres da string digitada é de: {len(frase)}')

print(f'{'-' * 10} ex. 01 {'-' * 10} ')
#chama a funçao e imprime a frase
mostra_frase(input('Digite uma frase: '))

##### EXEMPLO 02
#cria função com parametro
def mostra_frase_com_indice(frase):
    # usa o len para contar o numero de caracteres da frase e imprime
    print(f' A quantidade de  caracteres da string digitada é de: {len(frase)}')
    #usa loop for para pegar cada letra no seu indice, mais o indice e mostrar na tela com o print
    for i in range (len(frase)):
        print(f'Letra: {frase[i]} - {i}')

print(f'\n{'-' * 10} ex. 02 {'-' * 10} ')
#chama a funçao e imprime a frases
mostra_frase_com_indice(input('Digite uma frase: '))