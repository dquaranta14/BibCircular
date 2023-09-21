from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
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

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
