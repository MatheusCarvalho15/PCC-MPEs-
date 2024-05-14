
from django.forms import ModelForm
from .models import Despesa

class DespesasForm(ModelForm):

    class Meta:
        model = Despesa
        fields = '__all__'