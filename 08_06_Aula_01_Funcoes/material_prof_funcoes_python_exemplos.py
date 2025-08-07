# ============================================================================
# FUNÇÕES EM PYTHON - TODOS OS TIPOS DE IMPLEMENTAÇÃO
# ============================================================================

print("="*80)
print("EXEMPLOS COMPLETOS DE FUNÇÕES EM PYTHON")
print("="*80)

# ============================================================================
# 1. FUNÇÃO SEM PARÂMETROS E SEM RETORNO
# ============================================================================

# def saudacao_simples():
#     """Função mais básica - apenas executa uma ação"""
#     print("Olá! Bem-vindo ao curso de Python!")
#     print("Esta função não recebe parâmetros e não retorna nada")

# print("\n1. FUNÇÃO SEM PARÂMETROS E SEM RETORNO:")
# print("-" * 50)
# saudacao_simples()










# ============================================================================
# 2. FUNÇÃO SEM PARÂMETROS E COM RETORNO
# ============================================================================

# def obter_data_atual():
#     """Função que não recebe parâmetros mas retorna um valor"""
#     from datetime import datetime
#     return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# def obter_numero_aleatorio():
#     """Outro exemplo de função sem parâmetros com retorno"""
#     import random
#     return random.randint(1, 100)

# print("\n2. FUNÇÃO SEM PARÂMETROS E COM RETORNO:")
# print("-" * 50)
# data = obter_data_atual()
# numero = obter_numero_aleatorio()
# print(f"Data atual: {data}")
# print(f"Número aleatório: {numero}")











# ============================================================================
# 3. FUNÇÃO COM PARÂMETROS E SEM RETORNO
# ============================================================================

# def exibir_informacoes(nome, idade, cidade):
#     """Função que recebe parâmetros mas não retorna valor"""
#     print(f"Nome: {nome}")
#     print(f"Idade: {idade} anos")
#     print(f"Cidade: {cidade}")
#     print("Informações exibidas com sucesso!")

# def cumprimentar_pessoa(nome, tratamento="Sr(a)"):
#     """Função com parâmetro opcional"""
#     print(f"Olá {tratamento} {nome}, seja bem-vindo(a)!")

# print("\n3. FUNÇÃO COM PARÂMETROS E SEM RETORNO:")
# print("-" * 50)
# exibir_informacoes("João Silva", 30, "São Paulo")
# print()
# cumprimentar_pessoa("Maria")
# cumprimentar_pessoa("Ana", "Dra.")









# ============================================================================
# 4. FUNÇÃO COM PARÂMETROS E COM RETORNO
# ============================================================================

# def calcular_area_retangulo(largura, altura):
#     """Função que recebe parâmetros e retorna um valor"""
#     area = largura * altura
#     return area

# def calcular_imc(peso, altura):
#     """Função que calcula o IMC e retorna o valor e classificação"""
#     imc = peso / (altura ** 2)
    
#     if imc < 18.5:
#         classificacao = "Abaixo do peso"
#     elif imc < 25:
#         classificacao = "Peso normal"
#     elif imc < 30:
#         classificacao = "Sobrepeso"
#     else:
#         classificacao = "Obesidade"
    
#     return imc, classificacao

# print("\n4. FUNÇÃO COM PARÂMETROS E COM RETORNO:")
# print("-" * 50)
# area = calcular_area_retangulo(5, 3)
# print(f"Área do retângulo: {area} m²")

# imc_valor, imc_classe = calcular_imc(70, 1.75)
# print(f"IMC: {imc_valor:.2f} - {imc_classe}")








# ============================================================================
# ============================================================================
# 5. TIPOS DE PARÂMETROS
# ============================================================================
# ============================================================================

# print("\n" + "="*80)
# print("TIPOS DE PARÂMETROS EM FUNÇÕES")
# print("="*80)

# 5.1 PARÂMETROS POSICIONAIS
# def somar_tres_numeros(a, b, c):
#     """Parâmetros posicionais obrigatórios"""
#     return a + b + c

# print("\n5.1 PARÂMETROS POSICIONAIS:")
# print("-" * 40)
# resultado = somar_tres_numeros(10, 20, 30)
# print(f"Soma: 10 + 20 + 30 = {resultado}")




# ============================================================================
# 5.2 PARÂMETROS COM VALORES PADRÃO (DEFAULT)
# def criar_perfil(nome, idade, profissao="Estudante", ativo=True):
#     """Parâmetros com valores padrão"""
#     status = "Ativo" if ativo else "Inativo"
#     return f"{nome}, {idade} anos, {profissao} - Status: {status}"

# print("\n5.2 PARÂMETROS COM VALORES PADRÃO:")
# print("-" * 40)
# print(criar_perfil("Carlos", 22))  # Usando valores padrão
# print(criar_perfil("Ana", 25, "Engenheira"))  # Sobrescrevendo profissão
# print(criar_perfil("Bruno", 30, "Designer", False))  # Todos os parâmetros




# ============================================================================
# 5.3 PARÂMETROS NOMEADOS (KEYWORD ARGUMENTS)
# def calcular_desconto(preco, desconto_percentual=0, desconto_fixo=0):
#     """Função que pode ser chamada com parâmetros nomeados"""
#     desconto_total = (preco * desconto_percentual / 100) + desconto_fixo
#     preco_final = preco - desconto_total
#     return preco_final

# print("\n5.3 PARÂMETROS NOMEADOS:")
# print("-" * 40)
# preco_original = 100

# # Diferentes formas de chamar a função
# print(f"Preço original: R$ {preco_original}")
# print(f"Com 10% desconto: R$ {calcular_desconto(preco_original, desconto_percentual=10)}")
# print(f"Com R$ 15 desconto: R$ {calcular_desconto(preco_original, desconto_fixo=15)}")
# print(f"Com ambos os descontos: R$ {calcular_desconto(preco_original, desconto_percentual=10, desconto_fixo=5)}")








# 5.4 *ARGS - ARGUMENTOS VARIÁVEIS POSICIONAIS
# def calcular_media(*numeros):
#     """Função que aceita qualquer quantidade de números"""
#     if not numeros:
#         return 0
    
#     total = sum(numeros)
#     media = total / len(numeros)
#     return media

# print("\n5.4 *ARGS - ARGUMENTOS VARIÁVEIS:")
# print("-" * 40)
# print(f"Média de 10, 20: {calcular_media(10, 20)}")
# print(f"Média de 5, 10, 15, 20: {calcular_media(5, 10, 15, 20)}")
# print(f"Média de 8, 9, 7, 10, 6, 8: {calcular_media(8, 9, 7, 10, 6, 8)}")

# def listar_compras(titulo, *itens):
#     """Combinando parâmetro normal com *args"""
#     print(f"\n{titulo}:")
#     for i, item in enumerate(itens, 1):
#         print(f"  {i}. {item}")

# listar_compras("Lista de Supermercado", "Arroz", "Feijão", "Açúcar", "Café", "Leite")








# 5.5 **KWARGS - ARGUMENTOS VARIÁVEIS NOMEADOS
# def criar_conta(**dados):
#     """Função que aceita qualquer quantidade de parâmetros nomeados"""
#     print("\nConta criada com os seguintes dados:")
#     for chave, valor in dados.items():
#         print(f"  {chave.capitalize()}: {valor}")
#     return len(dados)

# print("\n5.5 **KWARGS - ARGUMENTOS NOMEADOS VARIÁVEIS:")
# print("-" * 40)
# campos = criar_conta(
#     nome="Pedro Santos",
#     email="pedro@email.com",
#     telefone="(11) 99999-9999",
#     endereco="Rua das Flores, 123",
#     cidade="São Paulo"
# )
# print(f"Total de campos preenchidos: {campos}")








# 5.6 COMBINANDO TODOS OS TIPOS
# def funcao_completa(obrigatorio, padrao="valor_padrao", *args, **kwargs):
#     """Função que combina todos os tipos de parâmetros"""
#     print(f"\nParâmetro obrigatório: {obrigatorio}")
#     print(f"Parâmetro com padrão: {padrao}")
    
#     if args:
#         print(f"Argumentos posicionais extras: {args}")
    
#     if kwargs:
#         print("Argumentos nomeados extras:")
#         for chave, valor in kwargs.items():
#             print(f"  {chave}: {valor}")

# print("\n5.6 COMBINANDO TODOS OS TIPOS:")
# print("-" * 40)
# funcao_completa(
#     "Este é obrigatório",
#     "Valor customizado",
#     "extra1", "extra2", "extra3",
#     categoria="exemplo",
#     versao=1.0,
#     ativo=True
# )











# ============================================================================
# 6. EXEMPLOS PRÁTICOS AVANÇADOS
# ============================================================================

# print("\n" + "="*80)
# print("EXEMPLOS PRÁTICOS AVANÇADOS")
# print("="*80)

# 6.1 FUNÇÃO QUE RETORNA MÚLTIPLOS VALORES
# def analisar_vendas(vendas):
#     """Análise completa de uma lista de vendas"""
#     total = sum(vendas)
#     media = total / len(vendas) if vendas else 0
#     maior = max(vendas) if vendas else 0
#     menor = min(vendas) if vendas else 0
    
#     return total, media, maior, menor

# print("\n6.1 FUNÇÃO COM MÚLTIPLOS RETORNOS:")
# print("-" * 40)
# vendas_mes = [1500, 2300, 1800, 2100, 1900, 2500, 1700]
# total, media, maior, menor = analisar_vendas(vendas_mes)

# print(f"Vendas do mês: {vendas_mes}")
# print(f"Total: R$ {total:.2f}")
# print(f"Média: R$ {media:.2f}")
# print(f"Maior venda: R$ {maior:.2f}")
# print(f"Menor venda: R$ {menor:.2f}")






# 6.2 FUNÇÃO COM VALIDAÇÃO DE DADOS
# def validar_e_processar_idade(idade_str, nome="Usuário"):
#     """Função que valida entrada e processa dados"""
#     try:
#         idade = int(idade_str)
        
#         if idade < 0:
#             return f"Erro: {nome}, idade não pode ser negativa!"
#         elif idade > 150:
#             return f"Erro: {nome}, idade muito alta!"
#         elif idade < 18:
#             return f"{nome} é menor de idade ({idade} anos)"
#         else:
#             return f"{nome} é maior de idade ({idade} anos)"
            
#     except ValueError:
#         return f"Erro: '{idade_str}' não é uma idade válida!"

# print("\n6.2 FUNÇÃO COM VALIDAÇÃO:")
# print("-" * 40)
# print(validar_e_processar_idade("25", "João"))
# print(validar_e_processar_idade("16", "Maria"))
# print(validar_e_processar_idade("abc", "Pedro"))
# print(validar_e_processar_idade("-5"))








# 6.3 FUNÇÃO COMO PARÂMETRO (HIGHER-ORDER FUNCTION)
# def aplicar_operacao(lista_numeros, operacao):
#     """Função que recebe outra função como parâmetro"""
#     return [operacao(num) for num in lista_numeros]

# def quadrado(x):
#     return x ** 2

# def cubo(x):
#     return x ** 3

# def dobrar(x):
#     return x * 2

# print("\n6.3 FUNÇÃO COMO PARÂMETRO:")
# print("-" * 40)
# numeros = [1, 2, 3, 4, 5]
# print(f"Números originais: {numeros}")
# print(f"Quadrados: {aplicar_operacao(numeros, quadrado)}")
# print(f"Cubos: {aplicar_operacao(numeros, cubo)}")
# print(f"Dobrados: {aplicar_operacao(numeros, dobrar)}")








# 6.4 FUNÇÃO LAMBDA (FUNÇÃO ANÔNIMA)
# print("\n6.4 FUNÇÕES LAMBDA:")
# print("-" * 40)

# # Lambdas simples
# multiplicar_por_3 = lambda x: x * 3
# eh_par = lambda x: x % 2 == 0

# print(f"5 multiplicado por 3: {multiplicar_por_3(5)}")
# print(f"8 é par? {eh_par(8)}")
# print(f"7 é par? {eh_par(7)}")





# Lambda com múltiplos parâmetros
# somar = lambda a, b: a + b
# print(f"Soma de 10 + 15: {somar(10, 15)}")

# # Lambda em aplicações práticas
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# quadrados = list(map(lambda x: x ** 2, numeros))

# print(f"Números: {numeros}")
# print(f"Apenas pares: {pares}")
# print(f"Quadrados: {quadrados}")








# ============================================================================
# 7. FUNÇÃO RECURSIVA 
# ============================================================================

# def fatorial(n):
#     """Exemplo de função recursiva"""
#     if n <= 1:
#         return 1
#     return n * fatorial(n - 1)

# def fibonacci(n):
#     """Sequência de Fibonacci usando recursão"""
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print("\n7. FUNÇÕES RECURSIVAS (BÔNUS):")
# print("-" * 40)
# print(f"Fatorial de 5: {fatorial(5)}")
# print(f"Sequência Fibonacci até 10: {[fibonacci(i) for i in range(10)]}")

# print("\n" + "="*80)
# print("RESUMO: TODOS OS TIPOS DE FUNÇÕES FORAM DEMONSTRADOS!")
# print("="*80)



