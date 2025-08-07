#4- Crie uma função que
# 1. leia e retorne o nome de uma pessoa (atribua a uma variável).
# 3. Crie outra função que receba como parâmetro o nome lido,
# 4. leia e retorne a idade para esse nome.
from operator import index


#cria funcao com parametro que recebe o nome e com retorno
def le_nome(nome):
    return nome

#cria listas com nomes e idades:
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
idades = [23, 31, 19, 27, 35]


# EXEMPLO 01 - COM PARAMETRO cria funcao que receba como parâmetro o nome lido, leia o nome e retorna a idade para esse nome.

#cria funcao com parametro
def atribui_idade_parametro(nome_lido_parametro):
    #se o nome estiver na lista, irá exibir a idade
    if nome_lido_parametro in nomes:
        print(f'{nome_lido_parametro}, o nome está na lista! ')
        index_nome = nomes.index(nome_lido_parametro)
    #caso contrário irá adicionar o nome na lista e pedir a idade para também adiconar na lista
    else:
        print(f'{nome_lido_parametro}, seu nome não está na lista!')
        #add nome na lista com append
        nomes.append(nome_lido_parametro)
        idade = int(input('Digite sua idade: '))
        # add idade na lista com append
        idades.append(idade)
        print('Contato adicionado com sucesso!')

#chama funcao com parametro
atribui_idade_parametro('Vitoria')

# usa o for para exibir a lista e verificar se os dados foram adicionados corretamente
for i in range(len(nomes)):
    print(f'Contato: {nomes[i]} - {idades[i]}')

print('-' * 20)

#EXEMPLO 02 - COM LISTA, SEM PARAMETRO - cria funcao que receba **como parâmetro o nome lido** SEM PARAMETRO, leia o nome e retorne a idade para esse nome.

#pede ao usuario para entrar com um nome
nome_lido = le_nome(input('\nDigite seu nome: '))

#def idade(nome_lido):
def atribui_idade():
    if nome_lido in nomes:
        print(f'{nome_lido}, o nome está na lista! ')
        index_nome = nomes.index(nome_lido)
        print(f'Sua idade é: {idades[index_nome]} anos de idade.')
    else:
        print(f'{nome_lido}, seu nome não está na lista!')
        nomes.append(nome_lido)
        idade = int(input('Digite sua idade: '))
        idades.append(idade)
        print('Contato adicionado com sucesso!')
        index_nome = nomes.index(nome_lido)
        print(f'{nome_lido}, sua idade é: {idades[index_nome]} anos de idade.')

#chama funcao sem parametro
atribui_idade()
# usa o for para exibir a lista e verificar se os dados foram adicionados corretamente
for i in range(len(nomes)):
    print(f'Contato: {nomes[i]} - {idades[i]}')
