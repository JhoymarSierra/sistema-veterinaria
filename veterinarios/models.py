
from django.db import models


class Veterinario(models.Model):
    pk_vet_id = models.AutoField(primary_key=True)
    tarjeta_profesional = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
