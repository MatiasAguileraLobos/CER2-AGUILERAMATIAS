from django.contrib import admin
from .models import PropuestaProyecto
from .models import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'rol']

admin.site.register(PropuestaProyecto)
