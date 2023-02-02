from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=250)
    raza = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=350)

    def __str__(self):
        return self.name
