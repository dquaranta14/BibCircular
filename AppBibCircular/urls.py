from django.urls import path
from AppBibCircular.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('lista-categorias/', lista_categorias, name='ListaCategorias'),
    path('lista-libros/', lista_libros, name='ListaLibros'),
    path('lista-lectores/', lista_lectores, name='ListaLectores'),
    path('lista-eventos/', lista_eventos, name='ListaEventos'),
    path('form-categoria/', categoria_formulario, name='CategoriaFormulario'),
    path('form-libro/', libro_formulario, name='LibroFormulario'),
    path('form-lector/', lector_formulario, name='LectorFormulario'),
    path('form-evento/', evento_formulario, name='EventoFormulario'),
    path('busqueda-libro/', busqueda_libro, name="BusquedaLibro"),
    path('buscar-libro/', buscar_libro, name="BuscarLibro"),
    path('buscar-lector/', buscar_lector, name="BuscarLector")
]