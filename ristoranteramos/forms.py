from django import forms
from .models import Usuario
from .models import ArticuloCarta

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','email','telefono','rol']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'autofocus': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]{9}',
            }),

            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = ArticuloCarta
        fields = ['nombre','ingredientes','categoria','precio','foto','receta','tiempo_estimado']
        widgets={
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'autofocus': True
            }),
            'ingredientes': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control',
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'receta': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'tiempo_estimado': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            })
        }
