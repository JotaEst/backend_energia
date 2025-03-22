from django.db import models
from usuarios.models import UsuarioModel

# Create your models here.
class MedidorModel(models.Model):
    numero_serie = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(UsuarioModel, on_delete=models.PROTECT)
    ciudad = models.CharField(max_length=100)
    longitud = models.FloatField()
    latitud = models.FloatField()

    def __str__(self):
        return f'Medidor: {self.numero_serie}'