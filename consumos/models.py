from django.db import models
from medidores.models import MedidorModel

# Create your models here.
class ConsumoModel(models.Model):
    id_consumo = models.AutoField(primary_key=True)
    numero_serie = models.ForeignKey(MedidorModel, on_delete=models.PROTECT)
    consumo_kwh = models.FloatField()
    fecha_consumo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Medidor: {self.numero_serie} - {self.consumo_kwh} kWh'