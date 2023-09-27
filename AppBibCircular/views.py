from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied

from .models import  Categoria, Libro, Lector, Evento, Reserva, Comentario
from .forms import CategoriaFormulario, LibroFormulario, LectorFormulario, EventoFormulario, UserEditForm, ComentarioFormulario, ReservaFormulario
from datetime import date

from django.core.mail import send_mail


# Create your views here.
def inicio(req):

    return render(req, "inicio.html")

def lista_categorias(req):

    lista = Categoria.objects.all()

    return render(req, "lista_categorias.html", {"lista_categorias": lista})


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


# --------------------------------------------------------------
# ------------    LIBROS   -------------------------------------
# --------------------------------------------------------------
def lista_libros(req, start=1):

    cant_por_pagina = 8

    if req.GET.get("direction") == 'next':
        start += 1
    elif req.GET.get("direction") == 'before':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start)+1)*cant_por_pagina
    lista = Libro.objects.order_by("nombre").filter(disponible = True)[inicio:final]

    return render(req, "lista_libros.html", {"lista_libros": lista, "current_page": start})

class LibroList(PermissionRequiredMixin, ListView):
    permission_required = 'staff_member_required'
    login_url = 'Login'
    redirect_field_name = 'lista_libros_admin.html'

    model = Libro
    template_name = "lista_libros_admin.html"
    context_object_name = "libros"
    queryset = Libro.objects.order_by("nombre")


class LibroDetail(DetailView):
    model = Libro
    template_name = "libro_detail.html"
    context_object_name = "libro"

class LibroCreate(CreateView):  
    model = Libro
    template_name = "libro_create.html"
    fields = ("__all__")
    success_url = "/app-bibcircular/"

class LibroUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "libro_update.html"
    fields = ("__all__")
    success_url = "/app-bibcircular/"

class LibroDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "libro_delete.html"
    success_url = "/app-bibcircular/"


# --------------------------------------------------------------
# ------------    COMENTARIOS-----------------------------------
# --------------------------------------------------------------
# @login_required
def nuevo_comentario(req, id):

    libro = Libro.objects.get(id=id)

    if req.method == 'POST':

        info = req.POST

        miFormulario = ComentarioFormulario({
            "comentario": info["comentario"]
        })
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            comentario = Comentario(
                libro=libro, 
                comentario=data["comentario"], 
                fecha=date.today(),
                user=req.user
            )
            comentario.save()
            return render(req, "inicio.html", {"mensaje": "Comentario creado con éxito"})
        else:
            print(miFormulario.errors)
            return render(req, "libro_comentario.html", {"miFormulario": miFormulario, "id": libro.id})
            
    else:

        miFormulario = ComentarioFormulario()
        return render(req, "libro_comentario.html", {"miFormulario": miFormulario, "id": libro.id, "nombre": libro.nombre})


# --------------------------------------------------------------
# ------------    LECTORES   -----------------------------------
# --------------------------------------------------------------
class LectorList(PermissionRequiredMixin, ListView):
    permission_required = 'staff_member_required'
    login_url = 'Login'
    
    model = Lector
    template_name = "lector_list.html"
    context_object_name = "lectores"
    queryset = Lector.objects.order_by("apellido","nombre")

class LectorDetail(DetailView):
    model = Lector
    template_name = "lector_detail.html"
    context_object_name = "lector"

class LectorUpdate(UpdateView):
    model = Lector
    template_name = "lector_update.html"
    fields = ("nombre", "apellido", "email", "telefono")
    success_url = "/app-bibcircular/"

class LectorDelete(LoginRequiredMixin, DeleteView):
    model = Lector
    template_name = "lector_delete.html"
    success_url = "/app-bibcircular/"

def crea_lector(req):

    if req.method == 'POST':

        info = req.POST

        miFormulario = LectorFormulario({
            "nombre": info["nombre"],
            "apellido": info["apellido"],
            "email": info["email"],
            "telefono": info["telefono"]
        })
        
        userForm = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"]
        })

        if miFormulario.is_valid() and userForm.is_valid():

            data = miFormulario.cleaned_data
            data.update(userForm.cleaned_data)

            user = User(username=data["username"])
            user.first_name = data["nombre"]
            user.last_name = data["apellido"]
            user.email = data["email"]
            user.set_password(data["password1"])
            
            user.save()

            lector = Lector(
                nombre=data["nombre"], 
                apellido=data["apellido"], 
                email=data["email"],
                telefono=data["telefono"],
                user=user
            )
            lector.save()
            return render(req, "inicio.html", {"mensaje": "Lector creado con éxito"})
        else:
            print(miFormulario.errors)
            print(userForm.errors)
            return render(req, "lector_create.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = LectorFormulario()
        userForm = UserCreationForm()

        return render(req, "lector_create.html", {"miFormulario": miFormulario, "userForm": userForm})
    
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

class EventoCreate(LoginRequiredMixin, CreateView):
    model = Evento
    template_name = "evento_create.html"
    fields = ["nombre", "fecha", "horario", "descripcion"]
    success_url = "/app-bibcircular/"

class EventoUpdate(LoginRequiredMixin, UpdateView):
    model = Evento
    template_name = "evento_update.html"
    fields = ("__all__")
    success_url = "/app-bibcircular/"

class EventoDelete(LoginRequiredMixin, DeleteView):
    model = Evento
    template_name = "evento_delete.html"
    success_url = "/app-bibcircular/"


def buscar_libro(req):

    if req.GET["titulo"]:
        titulo = req.GET["titulo"]
        libros = Libro.objects.filter(nombre__icontains=titulo) | Libro.objects.filter(autor__icontains=titulo )
        if libros:
            return render(req, "resultado_busqueda_libro.html", {"libros": libros})
        else:
            return render(req, "resultado_busqueda_libro.html", {"mensaje": "No se encontro ningun libro"})
    else:
        return render(req, "resultado_busqueda_libro.html", {"mensaje": "No ingreso ningun dato para buscar"})


def buscar_lector(req):

    if req.GET["lector"]:
        lector = req.GET["lector"]
        lectores = Lector.objects.filter(nombre__icontains=lector) | Lector.objects.filter(apellido__icontains=lector )
        if lectores:
            return render(req, "resultado_busqueda_lector.html", {"lectores": lectores})
        else:
            return render(req, "resultado_busqueda_lector.html", {"mensaje": "No se encontro ningun lector"})
    else:
        return render(req, "resultado_busqueda_lector.html", {"mensaje": "No ingreso ningun dato para buscar"})

# --------------------------------------------------------------
# ------------    RESERVAS   -----------------------------------
# --------------------------------------------------------------
# @login_required
def reserva_libro(req, id):

    libro = Libro.objects.get(id=id)

    if req.method == 'POST':

        reserva = Reserva(
                libro=libro, 
                user=req.user, 
                fecha=date.today()
            )
        reserva.save()
            
        libro.disponible = False
        libro.save()
    
        send_mail(f'Reserva libro: {libro.nombre}',f'{req.user.first_name} {req.user.last_name} - usuario {req.user} \nHa revervado el libro: {libro.nombre} del vendedor: {libro.vendedor}','danielaquaranta14@gmail.com',['dquaranta@hotmail.com'])

        return render(req, "inicio.html", {"mensaje": "Reserva realizada con éxito"})
            
    else:
        return render(req, "libro_reserva.html", {"id": libro.id, "nombre": libro.nombre})
   

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
    