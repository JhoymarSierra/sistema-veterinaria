from django.contrib import admin
from aplicaciones_vacunas.models import AplicacionVacuna
from .models import Vacuna


class AplicacionVacunaInline(admin.TabularInline):
    model = AplicacionVacuna
    extra = 1


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('pk_vacuna_id', 'nombre', 'laboratorio')
    search_fields = ('nombre', 'laboratorio')
    list_filter = ('laboratorio',)
    inlines = [AplicacionVacunaInline]
