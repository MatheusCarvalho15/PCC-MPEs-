from django.urls import path
from . import views
from produtos.views import criar_produto, listarProduto

urlpatterns = [
    path("add/", views.criar_produto, name="criar"),
    path("", views.listarProduto, name="listar"),
    path("editar/<int:id_produto>", views.editar, name="atualizar"),
    path("deletar/<int:id_produto>", views.deletar, name="confirmar"),
    path("deletar/confirmar/<int:id_produto>", views.confirmarExcluir, name="confirmar"),
]
