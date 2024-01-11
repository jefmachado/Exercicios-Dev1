from .base import *
from django.core.exceptions import ValidationError

def validaNome(value):
    if len(value) < 10:
        raise ValidationError ("O tipo de conta deve ter ao menos 10 Caracters !!!")
    else:
        return value

def validaEmail(value):
    if len(value) < 10:
        raise ValidationError("O email cadastrado não é valido")
    else:
        return value


class Cliente(BaseModels):
    cod = models.CharField(max_length=10, verbose_name="codigo", help_text="Codigo do cliente")
    nome = models.CharField(max_length=100, verbose_name="Nome", help_text="Nome do Cliente", validators=[validaNome])
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF", help_text="CPf do cliente")
    email = models.CharField(max_length=100, verbose_name="E-mail", help_text="E-mail do Cliente", validators=[validaEmail])

    class Meta:
        abstract = False

    def __str__(self):
        rsp = f"Codigo do Cliente: {self.cod}, Nome: {self.nome},\n "
        rsp += f"CPF: {self.cpf}, E-mail: {self.email}"
        return rsp

    def get_clientes_by_nome(self, nome=""):
        try:
            clientes = Cliente.objects.filter(nome__icontains=nome)
            listNome = list(clientes)
            print("Nome encontrado")
            return listNome
        except Cliente.DoesNotExist:
            return None

    def get_clientes_by_cpf(self, cpf=""):
        try:
            cliente = Cliente.objects.get(cpf=cpf)
            print('Cliente encontrado')
            return cliente
        except Cliente.DoesNotExist:
            return None

    def set_saldo_by_conta(self, conta):
        pass
            

