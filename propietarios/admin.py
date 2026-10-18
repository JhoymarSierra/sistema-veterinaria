from django.contrib import admin
from .models import Propietario

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre_completo', 'telefono')
    search_fields = ('cedula', 'nombre_completo')