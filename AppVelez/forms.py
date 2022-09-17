from django import forms



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