from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
   
    data_nascimento = models.DateField(null=True, blank=True)
