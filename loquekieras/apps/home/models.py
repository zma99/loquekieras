from django.db import models


class Usuario(models.Model):
    usuario = models.CharField(max_length=15, primary_key=True) 
    email = models.EmailField(max_length=20, unique=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    vendedor =models.BooleanField()
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=15)
    provincia = models.CharField(max_length=15)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()