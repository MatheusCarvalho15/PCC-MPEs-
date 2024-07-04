from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    VENDEDOR = 'vendedor'
    CAIXA = 'caixa'
    FUNCIONARIO = 'funcionario'
    ESCOLHAS_CARGO = [
        (VENDEDOR, 'Vendedor'),
        (CAIXA, 'Caixa'),
        (FUNCIONARIO,'Funcionario')
    ]

    cargo = models.CharField(max_length=20, choices=ESCOLHAS_CARGO, blank=True, null=True)
