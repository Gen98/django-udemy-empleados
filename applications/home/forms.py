# Este archivo es para la personalizaci[on de los campos de nuestro modelo en los formularios]
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        # widgets es para personalizar los campos en el html
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese texto aqui',
                    'class': 'test'
                }
            )
        }

    #validaciones extra def clean_atributo, debe ir a la altura del class
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad

