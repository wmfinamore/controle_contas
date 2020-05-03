from django.db import models


class Conta(models.Model):
    nome = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.descricao