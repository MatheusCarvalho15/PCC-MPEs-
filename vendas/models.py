from django.db import models

# Create your models here.
class Venda(models.Model):
    data = models.DateField()
    quantidade_produto = models.CharField(max_length=10)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)


class Produto(models.Model):
    valor_venda = models.CharField(max_length=50)
    garantia = models.DateField()
    objetivo = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    fornecedor = models.CharField(max_length=100)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.IntegerField(primary_key=True)
    