from django import forms
from .models import *
#Registro de Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutosFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    marca = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    modelo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    motor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(required=False)

    class Meta:
        model= Auto
        fields="__all__"
        widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'marca': forms.TextInput(attrs={'class': 'form-control'}),
        'modelo': forms.TextInput(attrs={'class': 'form-control'}),
        'motor': forms.TextInput(attrs={'class': 'form-control'})
    }

class MensajeFormulario(forms.Form):
    mensaje=forms.CharField(max_length=100)

