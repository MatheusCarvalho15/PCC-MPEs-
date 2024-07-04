from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden



def group_required(groups, raise_exception=False):
    def check_perms(user):
        if isinstance(groups, list):
            group_names = groups
        else:
            group_names = [groups]

        if user.groups.filter(name__in=group_names).exists():
            return True

        if raise_exception:
            raise PermissionDenied

        # As the last resort, return forbidden response
        return False

    return user_passes_test(
        lambda u: check_perms(u) or HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    )

#executa apenas uma vez para criar os grupos quando abre a página home
def create_groups():
    if not Group.objects.exists():
        groupAdmin = Group(name='vendedor')
        groupAdmin.save()

        groupAdmin = Group(name='caixa')
        groupAdmin.save()

        groupAdmin = Group(name='funcionario')
        groupAdmin.save()

        groupAdmin = Group(name='administrador')
        groupAdmin.save()






