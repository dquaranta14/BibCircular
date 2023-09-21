from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import  Categoria, Libro, Lector, Evento, Ventas, Comentario
from .forms import CategoriaFormulario, LibroFormulario, LectorFormulario, EventoFormulario, UserEditForm
from datetime import date

# Create your views here.
def inicio(req):

    return render(req, "inicio.html")

def lista_categorias(req):

    lista = Categoria.objects.all()

    return render(req, "lista_categorias.html", {"lista_categorias": lista})

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
# --------------------------------------------------------------
# ------------    LIBROS   -------------------------------------
# --------------------------------------------------------------
def lista_libros(req, start=1):

    cant_por_pagina = 6

    if req.GET.get("direction") == 'next':
        start += 1
    elif req.GET.get("direction") == 'before':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start)+1)*cant_por_pagina
    lista = Libro.objects.all()[inicio:final]

    return render(req, "lista_libros.html", {"lista_libros": lista, "current_page": start})


class LibroList(ListView):
    model = Libro
    template_name = "lista_libros.html"
    context_object_name = "libros"
    queryset = Libro.objects.order_by("nombre").filter(disponible = True)

class LibroDetail(DetailView):
    model = Libro
    template_name = "libro_detail.html"
    context_object_name = "libro"

class LibroCreate(CreateView):  
    model = Libro
    template_name = "libro_create.html"
    fields = ("__all__")
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

# --------------------------------------------------------------
# ------------    LECTORES   -----------------------------------
# --------------------------------------------------------------
class LectorList(LoginRequiredMixin, ListView):
    model = Lector
    template_name = "lector_list.html"
    context_object_name = "lectores"
    queryset = Lector.objects.order_by("apellido","nombre")

class LectorDetail(DetailView):
    model = Lector
    template_name = "lector_detail.html"
    context_object_name = "lector"

class LectorCreate(CreateView):
    model = Lector
    template_name = "lector_create.html"
    fields = ["nombre", "apellido", "email", "telefono"]
    success_url = "/app-bibcircular/"

class LectorUpdate(UpdateView):
    model = Lector
    template_name = "lector_update.html"
    fields = ("__all__")
    success_url = "/app-bibcircular/"

class LectorDelete(DeleteView):
    model = Lector
    template_name = "lector_delete.html"
    success_url = "/app-bibcircular/"

# --------------------------------------------------------------
# ------------    EVENTOS    -----------------------------------
# --------------------------------------------------------------
class EventoList(ListView):
    model = Evento
    template_name = "evento_list.html"
    context_object_name = "eventos"
    queryset = Evento.objects.order_by("fecha")

class EventoDetail(DetailView):
    model = Evento
    template_name = "evento_detail.html"
    context_object_name = "evento"

class EventoCreate(CreateView):
    model = Evento
    template_name = "evento_create.html"
    fields = ["nombre", "fecha", "horario", "descripcion"]
    success_url = "/app-bibcircular/"

class EventoUpdate(UpdateView):
    model = Evento
    template_name = "evento_update.html"
    fields = ("__all__")
    success_url = "/app-bibcircular/"

class EventoDelete(DeleteView):
    model = Evento
    template_name = "evento_delete.html"
    success_url = "/app-bibcircular/"


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
    
# --------------------------------------------------------------
# ------------    USUARIOS   -----------------------------------
# --------------------------------------------------------------

def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})

        else:
            #return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
            return render(req, "login.html", {"miFomulario": miFormulario, "mensaje": "Datos invalidos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFomulario": miFormulario})

def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]

            miFormulario.save()

            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFomulario": miFormulario})

def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado con éxito"})
        else:
            return render(req, "editarPerfil.html", {"miFomulario": miFormulario})
    else:

        miFormulario = UserEditForm(instance=req.user)

        return render(req, "editarPerfil.html", {"miFomulario": miFormulario})
    
#def agregar_avatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": f"Avatar actualizado con éxito!"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miFomulario": miFormulario})