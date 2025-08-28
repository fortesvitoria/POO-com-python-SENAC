class Lampada:

    def __init__(self):
        self.estado = False     #True lâmpada ligada

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def visual(self):
        if self.estado:
            return "LIGADO"
        return "DESLIGADO"

    def status(self):
        return f"Lâmpada\nStatus: {self.visual()}"

    def __str__(self):
        return f"Lâmpada\nStatus: {self.estado}"


################################
lampada = Lampada()
print("Estado inicial")
print(lampada)

# print(lampada.estado)
# lampada.ligar()
# lampada.desligar()
# print(lampada.status())

