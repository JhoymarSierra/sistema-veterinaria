from django.db import models

class Propietario(models.Model):
    # Llave primaria explícita según el diagrama ER
    pk_pro_id = models.AutoField(primary_key=True)
    
    cedula = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre_completo} ({self.cedula})"