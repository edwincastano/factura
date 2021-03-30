from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    correo = models.EmailField(max_length = 30)

    def __str__(self):
        return self.nombre