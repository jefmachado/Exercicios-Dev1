from retangulo import Retangulo
from circulo import Circulo
from funcionario import Funcionario
print('=' * 40)
print('===== RETANGULO =====')
print('=' * 40)
novoretangulo = Retangulo(10,5)
novoretangulo.calcularArea()
novoretangulo.calcularPerimetro()
novoretangulo.lado2 = 7
novoretangulo.calcularArea()
novoretangulo.calcularPerimetro()
print('=' * 40)
doisnovoretangulo = Retangulo(20,10)
doisnovoretangulo.calcularArea()
doisnovoretangulo.calcularPerimetro()
doisnovoretangulo.lado2 = 17
doisnovoretangulo.calcularArea()
doisnovoretangulo.calcularPerimetro()
print('=' * 40)
tresnovoretangulo = Retangulo(30,20)
tresnovoretangulo.calcularArea()
tresnovoretangulo.calcularPerimetro()
tresnovoretangulo.lado2 = 21
tresnovoretangulo.calcularArea()
tresnovoretangulo.calcularPerimetro()
print('=' * 40)
quatronovoretangulo = Retangulo(40,30)
quatronovoretangulo.calcularArea()
quatronovoretangulo.calcularPerimetro()
quatronovoretangulo.lado2 = 35
quatronovoretangulo.calcularArea()
quatronovoretangulo.calcularPerimetro()
print('=' * 40)
cinconovoretangulo = Retangulo(50,25)
cinconovoretangulo.calcularArea()
cinconovoretangulo.calcularPerimetro()
cinconovoretangulo.lado2 = 30
cinconovoretangulo.calcularArea()
cinconovoretangulo.calcularPerimetro()
print('=' * 40)
print('===== CIRCULO =====')
print('=' * 40)
novocirculo = Circulo(10.0)
novocirculo.calcularArea()
novocirculo.calcularPerimetro()
novocirculo.raio = 4
novocirculo.calcularArea()
novocirculo.calcularPerimetro()
print('=' * 40)
doiscirculo = Circulo(8.0)
doiscirculo.calcularArea()
doiscirculo.calcularPerimetro()
doiscirculo.raio = 2
doiscirculo.calcularArea()
doiscirculo.calcularPerimetro()
print('=' * 40)
trescirculo = Circulo(20.0)
trescirculo.calcularArea()
trescirculo.calcularPerimetro()
trescirculo.raio = 10
trescirculo.calcularArea()
trescirculo.calcularPerimetro()
print('=' * 40)
quatrocirculo = Circulo(30.0)
quatrocirculo.calcularArea()
quatrocirculo.calcularPerimetro()
quatrocirculo.raio = 15
quatrocirculo.calcularArea()
quatrocirculo.calcularPerimetro()
print('=' * 40)
cincocirculo = Circulo(50.0)
cincocirculo.calcularArea()
cincocirculo.calcularPerimetro()
cincocirculo.raio = 25
cincocirculo.calcularArea()
cincocirculo.calcularPerimetro()
print('=' * 40)
print('===== FUNCIONARIO =====')
print('=' * 40)
novofuncionario = Funcionario("Luis", "Silva", 10, 25.50)
novofuncionario.nomeCompleto()
novofuncionario.calcularSalario()
novofuncionario.incrementarHoras(8)
novofuncionario.calcularSalario()
print('='*40)

funcionarios = [
    Funcionario("Ana", "Pereira", 120, 30.0),
    Funcionario("Miguel", "Oliveira", 150, 27.0),
    Funcionario("Sofia", "Silveira", 135, 28.0),
    Funcionario("Lucas", "Fernandes", 170, 26.0),
    Funcionario("Alice", "Santos", 130, 29.0),
    Funcionario("Pedro", "Ribeiro", 155, 31.0),
    Funcionario("Isabella", "Gomes", 110, 33.0),
    Funcionario("Gabriel", "Lima", 125, 32.0),
    Funcionario("Laura", "Vieira", 140, 34.0)
]
for funcionario in funcionarios:
    funcionario.nomeCompleto()
    funcionario.calcularSalario()
    print('='*40)