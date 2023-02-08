from django import forms

# Create your forms here.

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    empresa = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    email = forms.EmailField()

class ProyectoForm(forms.Form):
    codigo = forms.CharField(max_length=40)
    fecha_recibido = forms.DateField()
    plazo = forms.IntegerField()
    categoria = forms.CharField(max_length=40)

class ResponsableForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
