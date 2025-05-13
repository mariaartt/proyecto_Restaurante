from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm



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
        fields = [
            'nombre', 'descripcion', 'categoria', 'precio',
            'foto', 'receta', 'tiempo_preparacion'
        ]
        exclude = ['fecha_creacion', 'fecha_modificacion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'autofocus': True
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'receta': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'tiempo_preparacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
        }

class RegistroFormulario(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'forms_field-input',
            'placeholder': 'Contraseña',
            'required': 'required'
        })
    )
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'rol', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'forms_field-input',
                'placeholder': 'Correo electrónico',
                'required': 'required'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'forms_field-input',
                'placeholder': 'Nombre completo',
                'required': 'required'
            }),
            'rol': forms.Select(attrs={
                'class': 'forms_field-input',
                'placeholder': 'Rol',
                'required': 'required'
            }),
        }

class LoginFormulario(AuthenticationForm):
    username = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={
            'class': 'forms_field-input',
            'placeholder': 'Correo electrónico',
            'required': 'required',
            'autofocus': 'autofocus'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'forms_field-input',
            'placeholder': 'Contraseña',
            'required': 'required'
        })
    )