from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import EmailValidator, RegexValidator, validate_email

class CustomAuthenticationForm(AuthenticationForm):
    # esta clase agrega para el username una validacion de email al autentication form de django
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators.append(validate_email)

class InicioSesionForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        required=True,
        validators=[
            EmailValidator(
                message='Ingresa un email válido en el campo de email.'
            )
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'password')

class RegistroForm(UserCreationForm):
    username = forms.CharField(
        max_length=254,
        required=True,
        validators=[
            EmailValidator(
                message='Ingresa un email válido en el campo de email.'
            )
        ]
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        validators=[
            RegexValidator(
                r'^[a-zA-Z]+$',
                'Ingresa solo letras en el campo de nombre.'
            )
        ]
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        validators=[
            RegexValidator(
                r'^[a-zA-Z]+$',
                'Ingresa solo letras en el campo de apellido.'
            )
        ]
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2'
                  )
