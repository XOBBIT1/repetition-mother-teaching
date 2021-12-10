from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }