
from accounts.views import register
from django.urls import path
urlpatterns = [
    #cadastroForaDoSistema
    path('register/', register, name='register'),

]