from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    UnMed = models.CharField(max_length=20)
    CodBarra = models.CharField(max_length=50)
    ValorVenda = models.DecimalField(max_digits=10, decimal_places=2)
    ValorCompra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome