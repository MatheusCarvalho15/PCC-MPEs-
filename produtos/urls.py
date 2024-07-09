from django.urls import path
from . import views
from produtos.views import criar_produto, listarProduto

urlpatterns = [
    path("add/", views.criar_produto, name="criar_produto"),
    path("", views.listarProduto, name="listar_produto"),
    path("editar/<int:id_produto>", views.editar, name="atualizar_produto"),
    path("deletar/<int:id_produto>", views.deletar, name="confirmar_produto"),
    path("deletar/confirmar/<int:id_produto>", views.confirmarExcluir, name="confirmar_produto"),
]
