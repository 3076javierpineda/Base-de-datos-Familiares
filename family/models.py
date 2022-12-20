from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateField(null=True)
    informacion = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Fecha: {self.fecha} - mas informacion: {self.informacion}'
    

