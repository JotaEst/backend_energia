from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario