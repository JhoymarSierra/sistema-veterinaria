from django.db import models


class Vacuna(models.Model):
    pk_vacuna_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_vacuna'

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio})"
