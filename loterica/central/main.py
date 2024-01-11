from loterica.models.cliente import Cliente
from loterica.models.conta import Conta

def Main():
    novoCliente = Cliente("v12345", "Geraldin", "1234555656", "geraldindograuarrobaterra")
    novoCliente.save()
    novaConta = Conta(312313123, "1", "Corrente", "2525", 150, novoCliente)
    novaConta.save()
    novoCliente.get_clientes_by_cpf("1234555656")
    novoCliente.get_clientes_by_nome("geraldin")
