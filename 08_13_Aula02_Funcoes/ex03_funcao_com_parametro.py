"""
Crie uma função que receba um número inteiro como parâmetro e
retorne esse número invertido

"""
def numero_invertido(numero):
    numero_novo = str(numero)[::-1]   # transforma em string e inverte
    print(int(numero_novo))           # volta pra inteiro

numero_invertido(15)  # saída: 51