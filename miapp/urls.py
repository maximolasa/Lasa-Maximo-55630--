from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertar-datos/', views.insertar_datos, name='insertar_datos'),
    path('buscar/', views.buscar, name='buscar'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.profile_edit, name='profile_edit'),
    path('aboutMe/', views.about_me, name='about_me'),
    
    
]
