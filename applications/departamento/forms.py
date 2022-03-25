from django import forms

class NewDepartamentoForm(forms.Form):
    """Form definition for NewDepartamento."""
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=20)

