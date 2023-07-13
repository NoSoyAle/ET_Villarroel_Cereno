#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Tienda 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda 
        fields = ['codigo', 'descripcion', 'precio', 'stock', 'imagen']
        labels = {
            'codigo' : "Codigo",
            'descripcion' : "Descripcion",
            'precio' : "Precio",
            'stock' : "Stock",
            'imagen' : "Imagen",

        }
        widgets={
            'codigo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el codigo',
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese una descripcion',
                    'class' : 'form-control',
                    'id' : 'descripcion'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el precio',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'stock':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el stock',
                    'class' : 'form-control',
                    'id' : 'stock'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            )
        }