from django.urls import path
from django.contrib.auth.views import LogoutView
from AppBibCircular.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('lista-categorias/', lista_categorias, name='ListaCategorias'),
    #path('lista-lectores/', lista_lectores, name='ListaLectores'),
    #path('lista-eventos/', lista_eventos, name='ListaEventos'),
    path('form-categoria/', categoria_formulario, name='CategoriaFormulario'),
    #path('form-libro/', libro_formulario, name='LibroFormulario'),
    #path('lista-libros/', LibroList.as_view(), name="ListaLibros"),
    path('lista-libros/<int:start>', lista_libros, name='ListaLibros'),
    path('detalle-libro/<pk>', LibroDetail.as_view(), name="DetalleLibros"),
    path('crea-libro/', LibroCreate.as_view(), name="CreaLibros"),
    path('actualiza-libro/<pk>', LibroUpdate.as_view(), name="ActualizaLibros"),
    path('elimina-libro/<pk>', LibroDelete.as_view(), name="EliminaLibros"),
    path('lista-lectores/', LectorList.as_view(), name="ListaLectores"),
    path('detalle-lector/<pk>', LectorDetail.as_view(), name="DetalleLectores"),
    path('crea-lector/', LectorCreate.as_view(), name="CreaLectores"),
    path('actualiza-lector/<pk>', LectorUpdate.as_view(), name="ActualizaLectores"),
    path('elimina-lector/<pk>', LectorDelete.as_view(), name="EliminaLectores"),
    path('lista-eventos/', EventoList.as_view(), name="ListaEventos"),
    path('detalle-evento/<pk>', EventoDetail.as_view(), name="DetalleEventos"),
    path('crea-evento/', EventoCreate.as_view(), name="CreaEventos"),
    path('actualiza-evento/<pk>', EventoUpdate.as_view(), name="ActualizaEventos"),
    path('elimina-evento/<pk>', EventoDelete.as_view(), name="EliminaEventos"),
    #path('form-lector/', lector_formulario, name='LectorFormulario'),
    path('busqueda-libro/', busqueda_libro, name="BusquedaLibro"),
    path('buscar-libro/', buscar_libro, name="BuscarLibro"),
    path('buscar-lector/', buscar_lector, name="BuscarLector"),

    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),
]