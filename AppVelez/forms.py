from django import forms



class plenoForm(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    genero=forms.CharField(max_length=25)
    edad=forms.IntegerField()
    documento=forms.IntegerField()
    email=forms.EmailField()
    direccion=forms.CharField(max_length=50)
    localidad=forms.CharField(max_length=50)
    provincia=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=50)
    numero_socio=forms.IntegerField()

class semiPlenoForm(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    genero=forms.CharField(max_length=25)
    edad=forms.IntegerField()
    documento=forms.IntegerField()
    email=forms.EmailField()
    direccion=forms.CharField(max_length=50)
    localidad=forms.CharField(max_length=50)
    provincia=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=50)
    numero_socio=forms.IntegerField()

class empleadoform(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    genero=forms.CharField(max_length=25)
    edad=forms.IntegerField()
    documento=forms.IntegerField()
    email=forms.EmailField()
    direccion=forms.CharField(max_length=50)
    localidad=forms.CharField(max_length=50)
    provincia=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=50)
    cargo=forms.CharField(max_length=50)
    sueldo=forms.IntegerField()
    legajo=forms.IntegerField()