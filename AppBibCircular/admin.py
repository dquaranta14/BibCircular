from django.contrib import admin
from .models import Categoria, Libro, Lector, Ventas, Evento

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Ventas)
admin.site.register(Evento)
