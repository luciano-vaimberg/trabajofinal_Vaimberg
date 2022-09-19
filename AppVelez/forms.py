from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class plenoForm(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    numero_socio=forms.IntegerField()

class semiPlenoForm(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    numero_socio=forms.IntegerField()

class empleadoform(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    legajo=forms.IntegerField()


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]
        help_texts = {k:"" for k in fields}
        

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)        
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)        
    first_name= forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Modificar Apellido")



    class Meta:
        model = User
        fields = ["email","password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}
        


class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")        