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
                'autofocus': True,
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '[0-9]{9}',
                'required': 'required'
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
            'imagen_url', 'receta', 'tiempo_preparacion'
        ]
        exclude = ['fecha_creacion', 'fecha_modificacion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'autofocus': True,
                'required': 'required'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
                'required': 'required'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'imagen_url': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': 'https?://.+',
                'title': 'Introduce una URL que comience con http:// o https://'
            }),
            'receta': forms.Textarea(attrs={
                'class': 'form-control',
                'required': 'required',
            }),
            'tiempo_preparacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': 'required'
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

    rol = forms.ChoiceField(
        choices=Usuario._meta.get_field('rol').choices,
        required=False,  # ← Esto hace que el rol no sea obligatorio
        widget=forms.Select(attrs={
            'class': 'forms_field-input',
            'placeholder': 'Rol'
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
            })
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

class FormularioFoto(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto']
        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class FormularioEditarPerfil(forms.ModelForm):
    class Meta:
        model = Usuario  # Enlazamos el formulario con el modelo 'Usuario'
        fields = ['nombre', 'telefono', 'direccion']  # Los campos a editar
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }