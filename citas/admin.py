
from django.contrib import admin
from .models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'pk_cita_id',
        'mascota',
        'veterinario',
        'fecha',
        'motivo',
    )
    search_fields = (
        'mascota__nombre',
        'veterinario__nombre',
        'motivo',
    )
    list_filter = ('fecha', 'veterinario')
    date_hierarchy = 'fecha'
