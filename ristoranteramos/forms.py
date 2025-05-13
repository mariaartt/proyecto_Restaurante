from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

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