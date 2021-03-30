from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    cliente = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 60)
    articulo = models.AutoField(max_length = 60)
    cantidad = models.AutoField(max_length = 30)
    valor unitario = models.CharField(max_length = 30)
    valor total = models.CharField(max_length = 30)


    def __str__(self):
        return self.nombre