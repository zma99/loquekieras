from django.db import models


class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    id = models.AutoField(primary_key = True)
    precio = models.IntegerField(default = 0)

    

class Usuario(models.Model):
    usuario = models.CharField(max_length=15, primary_key = True, unique = True) 
    email = models.EmailField(max_length=20)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    fecha_Nacimiento= models.DateField()
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=15)
    provincia = models.CharField(max_length=15)

