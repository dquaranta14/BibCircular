from django.contrib import admin
from .models import Categoria, Libro, Lector, Reserva, Evento, Comentario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Reserva)
admin.site.register(Evento)
admin.site.register(Comentario)
