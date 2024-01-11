from .base import *


class Jogador (BaseModel):
    nome = models.CharField(max_length=150, verbose_name="Nome", help_text="Nome do Jogador")
    apelido = models.CharField(max_length=150, verbose_name="Apelido", help_text="Apelido do Jogador")
    dataNascimento = models.DateField(verbose_name="Data de Nascimento", help_text="Data de Nascimento do Jogador")
    numero = models.IntegerField(verbose_name="Numero", help_text="Numero do Jogador")
    posição = models.CharField(max_length=150, verbose_name="Posição", help_text="Posição do Jogador")
    qualidade = models.IntegerField(verbose_name="Qualidade", help_text="Posição do Jogador")
    cartoes = models.IntegerField(verbose_name="Cartões", help_text="Cartoes que o Jogador Possui")
    suspensao = models.BooleanField(default=False, verbose_name="Suspensao", help_text="Situação que o jogador se encontra")

    class Meta:
        abstract = False

    def __str__(self):
        str = f"""
        Nome do Jogador: {self.nome}, Data de Nascimento: {self.dataNascimento}
        Apelido do Jogador: {self.apelido}, Número: {self.numero}
        Posição: {self.posição}, Pontuação Geral: {self.qualidade}
        Cartoes: {self.cartoes}, suspensao: {self.suspensao}
        """
        return str

    def jogadores(self):
        listaJogadores = {
          'listaJogadore': Jogador.objects.all()
        }

        if not listaJogadores:
            print('Nenhum Jogador Cadastrado')
        else:
            for jogador in listaJogadores:
                print(jogador.__str__())

    def condicaoJogador(self):

        listasuspensa = Jogador.objects.filter(suspensao=True)

        if not listasuspensa:
            print('Nenhum Jogador Listado esta apto para jogar')
        else:
            for jogador in listasuspensa:
                 print(jogador.__str__())




