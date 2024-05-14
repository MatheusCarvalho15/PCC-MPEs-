from django.contrib import admin
from .models import Usuario

  

class UsuarioModelAdmin(admin.ModelAdmin):

    list_display = ['first_name',  'username']
    fields = ['username', 'first_name', 'password']

    def create(self):

        self.create()

admin.site.register(Usuario, UsuarioModelAdmin)
