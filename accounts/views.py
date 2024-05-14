
from django.shortcuts import render, redirect
from accounts.forms import usuariosForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = usuariosForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedidoio
                       
    else:
        form = usuariosForm()
    return render(request, 'registration/register.html', {'form': form})
