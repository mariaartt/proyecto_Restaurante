from django import forms
from .models import Empleado

class FormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'rol']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'autofocus': True
            }),
            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

