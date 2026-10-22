from django.db import models
 
 
class AplicacionVacuna(models.Model):
    pk_apv_id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(
        'mascotas.Mascota',   # <-- CAMBIAR si la app o el modelo de tu compañero se llaman distinto
        on_delete=models.CASCADE,
        db_column='fk_mas_id',
    )
    vacuna = models.ForeignKey(
        'vacunas.Vacuna',
        on_delete=models.CASCADE,
        db_column='fk_vac_id',
    )
    fecha_aplicacion = models.DateField()
    dosis = models.CharField(max_length=50)
 
    class Meta:
        db_table = 'tbl_aplicacion_vacuna'
 
    def _str_(self):
        return f"{self.mascota} - {self.vacuna} ({self.fecha_aplicacion})"
