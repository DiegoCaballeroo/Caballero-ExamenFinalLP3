from django.db import models

# Create your models here.
class Caballero_Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.BooleanField()
    fecha_de_registro = models.DateTimeField(auto_now_add=True)