from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):

    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    resena = models.TextField(null=True)
    precio = models.FloatField(null=True)

    def __str__(self):
        return self.nombre
   

class Lector(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta():
        verbose_name_plural = 'Lectores'

class Evento(models.Model):

    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    horario = models.TimeField()
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f'{self.nombre} - {self.fecha} {self.horario}'


class Ventas(models.Model):

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    importe = models.FloatField()

    def __str__(self):
        return f'{self.libro} - {self.lector} - {self.fecha}'
