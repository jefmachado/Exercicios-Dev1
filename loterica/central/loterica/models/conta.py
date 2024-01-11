from .base import *
from .cliente import Cliente
from django.core.exceptions import ValidationError

def validaTipo(value):
    if len(value) < 10:
        raise ValidationError ("O tipo de conta deve ter ao menos 10 Caracters !!!")
def validaSaldo(value):
    if value < 0:
        raise ValidationError ("O saldo inicial da conta não pode ser negativo !!!")

class Conta(BaseModels):
    numero = models.IntegerField(verbose_name="Número", help_text="Numero da Conta")
    digito = models.CharField(max_length=1, verbose_name="Digito", help_text="Digito da Conta bancaria")
    tipo = models.CharField(max_length=20, verbose_name="Tipo", help_text="Tipo de Conta Bancaria", validators=[validaTipo])
    agencia = models.CharField(max_length=4, verbose_name="Agencia", help_text="Agencia Bancaria")
    saldo = models.FloatField(verbose_name="Saldo", help_text="Saldo da Conta", validators=[validaSaldo])
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        abstract = False

    def __str__(self):
        rsp = f"Número da conta: {self.numero}, Digito: {self.digito},\n"
        rsp += f"Tipo: {self.tipo}, Agencia: {self.agencia}\n"
        rsp += f"Saldo Bancario: {self.saldo}"
        return rsp

    def get_contas_by_clientes(self, clientes):
        try:
            clientes = Conta.objects.filter(Cliente=clientes)
            listCliente = list(clientes)
            return listCliente
        except Cliente.DoesNotExist:
            return None

    def get_contas_by_agencia(self, agencia):
        try:
            agencias = Conta.objects.filter(agencia=agencia)
            listagencias = list(agencias)
            return listagencias
        except Cliente.DoesNotExist:
            return None