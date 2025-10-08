'''
Exercício:
Sistema de Monitoramento de Temperatura
========================================

Você foi contratado para desenvolver um sistema simples de monitoramento de
temperatura para uma estufa automatizada.

A classe Estufa deve armazenar a temperatura interna e permitir que ela
seja acessada e modificada.

Objetivo:
Implementar a classe Estufa utilizando o decorador @property
para controlar o acesso à temperatura.
A temperatura deve estar sempre entre 15°C e 35°C.
Se o valor estiver fora desse intervalo, uma exceção deve ser lançada.

Requisitos
Crie a classe Estufa com um atributo privado __temperatura.
Implemente um getter com @property que retorna a temperatura atual.
Implemente um setter com @temperatura.setter que:
Verifica se o valor está entre 15 e 35.
- Lança uma ValueError se estiver fora do intervalo.
- Adicione um método status() que retorna:
"Temperatura ideal" se estiver entre 20 e 30.
Caso contrário: "Temperatura fora do ideal".

####
Implemente também uma lógica de alerta automático
(um método que dispara um aviso se a
temperatura estiver fora do ideal por mais de 3
vezes consecutivas).

####
Adicionar uma classe Sensor que simula leituras aleatórias.
'''
import random

class Sensor:
    def __init__(self):
        self.__value = random.randint(0,50)
    
    @property
    def value(self):
        return self.__value

s = Sensor()

class Estufa:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    def status (self):
        if 20 <= self.__temperatura <= 30:
            print(f"Temperatura de {self.__temperatura}C, está ideal.")
        else:
            print(f"Temperatura {self.__temperatura}C está fora do ideal.")

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        self.__temperatura = nova_temperatura
        self.status

n = Estufa(s.value)
n.status()
        
