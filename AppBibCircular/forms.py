from django import forms
from .models import Libro

class CategoriaFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)

class LibroFormulario(forms.ModelForm):

    class Meta:
        model=Libro
        fields=('__all__')


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