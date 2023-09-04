from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm, ReviewForm
from .models import Producto, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, logout
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

def about_me(request):
    return render(request, 'aboutMe.html')


@login_required
def profile_edit(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = UserProfileForm(instance=user)

    context = {'form': form}
    return render(request, 'profile_edit.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, 'index.html')

def insertar_datos(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if categoria_form.is_valid() and producto_form.is_valid() and cliente_form.is_valid():
            categoria = categoria_form.save()
            producto = producto_form.save(commit=False)
            producto.categoria = categoria
            producto.save()
            cliente_form.save()

    else:
        categoria_form = CategoriaForm()
        producto_form = ProductoForm()
        cliente_form = ClienteForm()

    return render(request, 'insertar_datos.html', {
        'categoria_form': categoria_form,
        'producto_form': producto_form,
        'cliente_form': cliente_form,
    })



def buscar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        resultados = []

    return render(request, 'buscar.html', {'resultados': resultados})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})