from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    USUARIO_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Directivo', 'Directivo'),
        ('Estudiante', 'Estudiante'),
    ]
    usuario = forms.ChoiceField(choices=USUARIO_CHOICES)
    email = forms.CharField()  # Agrega esta línea

    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'usuario',  'semestre']


class SinusuarioForm(forms.ModelForm):
    USUARIO_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Directivo', 'Directivo'),
        ('Estudiante', 'Estudiante'),
    ]
    email = forms.CharField()  # Agrega esta línea

    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email',   'semestre']

# forms.py
class CambiarContrasenaForm(forms.ModelForm):
    USUARIO_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Directivo', 'Directivo'),
        ('Estudiante', 'Estudiante'),
    ]

    class Meta:
        model = Usuarios
        fields = ['password']

