import math

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = self.largura * self.altura
        return round(area,2)

class Triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return round(area,2)

class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        return round(area,2)

lista_formas = [Retangulo(30,10),Retangulo(20,10), Triangulo(10,20),Triangulo(10,30), Circulo(10), Circulo(20)]

def calcular_area(lista_formas):
    for forma in lista_formas:
        print(f"A área da forma {forma} é: {forma.calcular_area()}")

calcular_area(lista_formas)