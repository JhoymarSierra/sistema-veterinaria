from django.contrib import admin
from .models import Mascota
from historias_clinicas.models import HistoriaClinica

class HistoriaClinicaInline(admin.StackedInline):
    model = HistoriaClinica
    can_delete = False

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'propietario')
    search_fields = ('nombre', 'propietario__nombre_completo', 'propietario__cedula')
    list_filter = ('especie', 'raza')
    inlines = [HistoriaClinicaInline]