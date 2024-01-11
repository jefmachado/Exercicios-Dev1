class Funcionario:
    def __init__(self, nome="", sobrenome="", horasTrabalhadas=0, valorPorHora=0.0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horasTrabalhadas = horasTrabalhadas
        self.valorPorHora = valorPorHora

    def nomeCompleto(self):
        print(f'Nome completo: {self.nome} {self.sobrenome}')

    def calcularSalario(self):
        salario = self.horasTrabalhadas * self.valorPorHora
        print(f'Salário: R${salario:.2f}')

    def incrementarHoras(self, horas):
        self.horasTrabalhadas += horas