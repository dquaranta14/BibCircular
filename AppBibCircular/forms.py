from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Libro, Lector, Comentario, Reserva

class CategoriaFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)

class LectorFormulario(forms.ModelForm):

    class Meta:
        model = Lector
        fields = ('nombre', 'apellido', 'email', 'telefono')

class LibroFormulario(forms.ModelForm):

    class Meta:
        model=Libro
        fields=('__all__')

class ComentarioFormulario(forms.ModelForm):

    class Meta:
        model=Comentario
        fields=('comentario',)


class EventoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    lugar = forms.CharField(required=False)
    fecha = forms.DateField(required=True)
    horario = forms.TimeField(required=True)
    descripcion = forms.CharField(required=False)


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    passwordA = forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name','passwordA', 'password1', 'password2')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ReservaFormulario(forms.ModelForm):

       class Meta:
        model=Reserva
        fields=('__all__')