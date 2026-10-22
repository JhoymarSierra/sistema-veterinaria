from django.db import models

class Vacuna(models.Model):
    pk_vacuna_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_vacuna'

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio})"

class AplicacionVacuna(models.Model):
    pk_apv_id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(
        'mascotas.Mascota', 
        on_delete=models.CASCADE,
        db_column='fk_mas_id',
    )
    vacuna = models.ForeignKey(
        'Vacuna',
        on_delete=models.CASCADE,
        db_column='fk_vac_id',
    )
    fecha_aplicacion = models.DateField()
    dosis = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_aplicacion_vacuna'

    def __str__(self):
        return f"{self.mascota} - {self.vacuna} ({self.fecha_aplicacion})"