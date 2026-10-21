
from django.db import models
from mascotas.models import Mascota
from veterinarios.models import Veterinario


class Cita(models.Model):
    pk_cita_id = models.AutoField(primary_key=True)

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.PROTECT,
        db_column='fk_mas_id'
    )

    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.PROTECT,
        db_column='fk_vet_id'
    )

    fecha = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return (
            f"Cita {self.pk_cita_id} - "
            f"{self.mascota.nombre} - "
            f"{self.veterinario.nombre}"
        )
