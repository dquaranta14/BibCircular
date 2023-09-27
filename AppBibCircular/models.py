from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lector(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    class Meta():
        verbose_name_plural = 'Lectores'

class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):

    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    resena = models.TextField(null=True)
    precio = models.FloatField(null=True)
    vendedor = models.ForeignKey(Lector, on_delete=models.CASCADE, null=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='portadas', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.autor}'


class Comentario(models.Model):

    libro = models.ForeignKey(Libro, related_name='comentarios', on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.libro}, {self.fecha}'
    
class Evento(models.Model):

    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    horario = models.TimeField()
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f'{self.nombre} - {self.fecha} {self.horario}'

class Reserva(models.Model):

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return f'{self.libro} - {self.user} - {self.fecha}'
    class Meta():
        verbose_name_plural = 'Reservas'