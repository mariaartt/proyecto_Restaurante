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
                'class': 'form-select',
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