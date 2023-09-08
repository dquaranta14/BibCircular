from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import  Categoria, Libro, Lector, Evento, Ventas
from .forms import CategoriaFormulario, LibroFormulario, LectorFormulario, EventoFormulario


# Create your views here.
def inicio(req):

    return render(req, "inicio.html")

def lista_categorias(req):

    lista = Categoria.objects.all()

    return render(req, "lista_categorias.html", {"lista_categorias": lista})

""" def lista_libros(req):

    lista = Libro.objects.all()

    return render(req, "lista_libros.html", {"lista_libros": lista}) """

def lista_lectores(req):

    lista = Lector.objects.all()

    return render(req, "lista_lectores.html", {"lista_lectores": lista})

def lista_eventos(req):

    lista = Evento.objects.all()

    return render(req, "lista_eventos.html", {"lista_eventos": lista})

def categoria_formulario(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = CategoriaFormulario(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            categoria = Categoria(nombre=data["nombre"])
            categoria.save()
            return render(req, "inicio.html", {"mensaje": "Categoria creada con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = CategoriaFormulario()

        return render(req, "categoria_formulario.html", {"miFomulario": miFormulario})

""" def libro_formulario(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = LibroFormulario(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            #libro = Libro(nombre=data["nombre"], autor=data["autor"], categoria=data["categoria"], resena=data["resena"], precio=data["precio"])
            libro = Libro(nombre=data["nombre"], autor=data["autor"], resena=data["resena"], precio=data["precio"])
            libro.save()
            return render(req, "inicio.html", {"mensaje": "Libro creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = LibroFormulario()

        return render(req, "libro_formulario.html", {"miFomulario": miFormulario})
 """
class LibroList(ListView):
    model = Libro
    template_name = "libro_list.html"
    context_object_name = "libros"


class LibroDetail(DetailView):
    model = Libro
    template_name = "libro_detail.html"
    context_object_name = "libro"

class LibroCreate(CreateView):
    model = Libro
    template_name = "libro_create.html"
    fields = ["nombre", "autor", "categoria", "resena", "precio"]
    success_url = "/app-bibcircular/"

class LibroUpdate(UpdateView):
    model = Libro
    template_name = "libro_update.html"
    fields = ("__all__")
    success_url = "/app-bibcircular/"

class LibroDelete(DeleteView):
    model = Libro
    template_name = "libro_delete.html"
    success_url = "/app-bibcircular/"

def lector_formulario(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = LectorFormulario(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            lector = Lector(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], telefono=data["telefono"])
            lector.save()
            return render(req, "inicio.html", {"mensaje": "Lector creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = LectorFormulario()

        return render(req, "lector_formulario.html", {"miFomulario": miFormulario})

def evento_formulario(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = EventoFormulario(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            evento = Evento(nombre=data["nombre"], fecha=data["fecha"], horario=data["horario"], descripcion=data["descripcion"])
            evento.save()
            return render(req, "inicio.html", {"mensaje": "Evento creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = EventoFormulario()

        return render(req, "evento_formulario.html", {"miFomulario": miFormulario})


def busqueda_libro(req):

    return render(req, "busqueda_libro.html")

def buscar_libro(req):

    if req.GET["titulo"]:
        titulo = req.GET["titulo"]
        libros = Libro.objects.filter(nombre__icontains=titulo) | Libro.objects.filter(autor__icontains=titulo )
        if libros:
            return render(req, "resultado_busqueda_libro.html", {"libros": libros})
    else:
        return HttpResponse('No escribiste ningun titulo')


def busqueda_lector(req):

    return render(req, "busqueda_lector.html")

def buscar_lector(req):

    if req.GET["lector"]:
        lector = req.GET["lector"]
        lectores = Lector.objects.filter(nombre__icontains=lector) | Lector.objects.filter(apellido__icontains=lector )
        if lectores:
            return render(req, "resultado_busqueda_lector.html", {"lectores": lectores})
    else:
        return HttpResponse('No escribiste ningun nombre de lector')