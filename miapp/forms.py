from django import forms
from .models import Categoria, Producto, Cliente, Review  
from django.contrib.auth.models import User


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'categoria')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'email')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('juego', 'resena', 'calificacion')

        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)

   

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput(render_value=True), required=False)
