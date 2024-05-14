from django.db import models


class Despesa(models.Model):
    despesa = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.despesa) + " / ID: " + str(self.id)
