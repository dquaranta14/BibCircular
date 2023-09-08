from django.urls import path
from AppBibCircular.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('lista-categorias/', lista_categorias, name='ListaCategorias'),
    path('lista-lectores/', lista_lectores, name='ListaLectores'),
    path('lista-eventos/', lista_eventos, name='ListaEventos'),
    path('form-categoria/', categoria_formulario, name='CategoriaFormulario'),
    #path('form-libro/', libro_formulario, name='LibroFormulario'),
    path('lista-libros/', LibroList.as_view(), name="ListaLibros"),
    path('detalle-libro/<pk>', LibroDetail.as_view(), name="DetalleLibros"),
    path('crea-libro/', LibroCreate.as_view(), name="CreaLibros"),
    path('actualiza-libro/<pk>', LibroUpdate.as_view(), name="ActualizaLibros"),
    path('elimina-libro/<pk>', LibroDelete.as_view(), name="EliminaLibros"),

    path('form-lector/', lector_formulario, name='LectorFormulario'),
    path('form-evento/', evento_formulario, name='EventoFormulario'),
    path('busqueda-libro/', busqueda_libro, name="BusquedaLibro"),
    path('buscar-libro/', buscar_libro, name="BuscarLibro"),
    path('buscar-lector/', buscar_lector, name="BuscarLector")
]