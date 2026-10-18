from django.db import models
from propietarios.models import Propietario

class Mascota(models.Model):
    # Llave primaria explícita
    pk_mas_id = models.AutoField(primary_key=True)
    
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    
    # Llave foránea. Le ponemos db_column para forzar el nombre en la base de datos
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='fk_pro_id')

    def __str__(self):
        return f"{self.nombre} - Dueño: {self.propietario.nombre_completo}"