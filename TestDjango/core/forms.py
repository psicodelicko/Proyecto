
from dataclasses import fields
from re import M
from django import forms
from django.forms import ModelForm
from .models import Producto, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields =['idUsuario','nombres','apellidos','nombreUsuario','contrasena']

class RegistrarProducto(ModelForm):

    class Meta:
        model = Producto
        fields =['idProducto','nombreProducto','descripcionProducto','precioProducto','imagen','categoria']

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data


class CustomerUserCreationForm (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","password1","password2"]

class ModificarUsuario (ModelForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email"]

class CrearCuentaAdmin (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_superuser","password1","password2"]