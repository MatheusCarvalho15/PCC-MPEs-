from django.db import models

class Imposto(models.Model):
    motivo = models.CharField(max_length=200)
    destino = models.CharField(max_length=155)
    prazo = models.DateField()

