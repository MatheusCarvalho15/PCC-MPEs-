
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UsuariosForm, PermissionForm
from django.http import HttpResponseRedirect
from .models import Usuario
from MPEs.utils import create_groups, group_required
from django.contrib.auth.models import Group
# Create your views here.
def register(request):
    create_groups()
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            grupo = Group.objects.get(name='funcionario')
            grupo.user_set.add(user)
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedidoio
                       
    else:
        form = UsuariosForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def listarUsuarios(request):
    usuario = Usuario.objects.all()

    return render(request, "registration/listarUsuarios.html", {'usuario': usuario})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Usuario
from .forms import PermissionForm

@group_required(['administrador'], "/accounts/login/")
def editarUsuario(request, id_user):
    # Pega os dados como estão no banco
    usuario = get_object_or_404(Usuario, pk=id_user)

    # Verifica se estão chegando os dados
    if request.method == 'POST':
        # Como chegou os dados, carregar os dados no modelform
        form = PermissionForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()

            # Obtenha o cargo atualizado do formulário
            cargo = form.cleaned_data.get('cargo')

            try:
                # Limpa os grupos atuais do usuário
                usuario.groups.clear()

                # Obtém ou cria o grupo e adiciona o usuário ao novo grupo
                grupo, created = Group.objects.get_or_create(name=cargo)
                grupo.user_set.add(usuario)
            except Group.DoesNotExist:
                return HttpResponse(f"Grupo '{cargo}' não encontrado", status=404)

            return HttpResponseRedirect('/despesas/?msg=Salvo')
    else:
        form = PermissionForm(instance=usuario)

    return render(request, "registration/updateUsuario.html", {'form': form, 'id_user': id_user})


@group_required([''], "")
def deletarUsuario(request, id_user):
    usuario = Usuario.objects.get(pk=id_user).delete()

    return HttpResponseRedirect('/despesas/?msg=Excluido')