class Retangulo:
    def __init__(self, lado1=0.0, lado2=0.0):
        self.lado1 = lado1
        self.lado2 = lado2
        self.area = 0.0
        self.perimetro = 0.0

    def calcularArea(self):
        self.area = self.lado1 * self.lado2
        print(f'Área do retângulo: {self.area}')

    def calcularPerimetro(self):
        self.perimetro = 2 * (self.lado1 + self.lado2)
        print(f'Perímetro do retângulo: {self.perimetro}')