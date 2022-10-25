from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateField(null=True)# Create your models here.

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido}'
