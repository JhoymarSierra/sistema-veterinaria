
from django.contrib import admin
from .models import Veterinario


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = (
        'pk_vet_id',
        'tarjeta_profesional',
        'nombre',
        'especialidad',
    )
    search_fields = (
        'tarjeta_profesional',
        'nombre',
        'especialidad',
    )
    list_filter = ('especialidad',)
