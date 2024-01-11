import math

class Circulo:
    def __init__(self, raio=0.0):
        self.raio = raio
        self.area = 0.0
        self.perimetro = 0.0

    def calcularArea(self):
        self.area = math.pi * self.raio ** 2
        print(f'Área do círculo: {self.area:.2f}')

    def calcularPerimetro(self):
        self.perimetro = 2 * math.pi * self.raio
        print(f'Perímetro do círculo: {self.perimetro:.2f}')