from django.db import models
from mascotas.models import Mascota

class HistoriaClinica(models.Model):
    # La mascota funciona como llave primaria para asegurar la relación 1:1
    mascota = models.OneToOneField(Mascota, on_delete=models.CASCADE, primary_key=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    antecedentes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historia Clínica - {self.mascota.nombre}"