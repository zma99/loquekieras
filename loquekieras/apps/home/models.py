from django.db import models


class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    

