from django import forms

class CategoriaFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)

class LibroFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    autor = forms.CharField(required=True)
    #categoria = forms.CharField(required=False)
    resena = forms.CharField(required=False)
    precio = forms.FloatField(required=False)

class LectorFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=50)

class EventoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    fecha = forms.DateField(required=True)
    horario = forms.TimeField(required=True)
    descripcion = forms.CharField(required=False)