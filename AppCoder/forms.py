from django import forms

class ProfesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class BuscarProfe(forms.Form):
    apellido_profe = forms.CharField(max_length=30)

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class BuscarCamada(forms.Form):
    camada = forms.IntegerField()

class EstudFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class BuscarEstud(forms.Form):
    apellido_estud = forms.CharField(max_length=30)

class EntregFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField(required=False)

class BuscarEntreg(forms.Form):
    nombre_e = forms.CharField(max_length=20)