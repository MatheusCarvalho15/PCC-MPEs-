
from accounts.views import register
from accounts.views import listarUsuarios, editarUsuario, deletarUsuario
from django.urls import path
urlpatterns = [
    #cadastroForaDoSistema
    path('register/', register, name='register'),
    path('Usuarios/', listarUsuarios, name='listarUsuarios'),
    path('editarUsuario/<int:id_user>', editarUsuario, name='editarUsuario'),
    path('deletarUsuario/<int:id_user>', deletarUsuario, name='deletarUsuario')

]