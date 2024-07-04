from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Usuario

class UsuariosForm(UserCreationForm):


    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'data_nascimento', 'password1']




class PermissionForm(forms.ModelForm):
    VENDEDOR = 'vendedor'
    CAIXA = 'caixa'
    FUNCIONARIO = 'funcionario'
    ADMINISTRADOR = 'administrador'
    CHOICES = [
        (VENDEDOR, 'Vendedor'),
        (CAIXA, 'Caixa'),
        (FUNCIONARIO,'Funcionario')
        (ADMINISTRADOR,'administrador')
    ]

    cargo = forms.ChoiceField(
        label='Cadastrar:',
        choices=CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Usuario
        fields = ['cargo']