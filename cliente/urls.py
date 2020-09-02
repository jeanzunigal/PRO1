from django.contrib import admin
from django.urls import path, include
from cliente import views
urlpatterns = [
    path('cliente/', views.cliente, name="cliente"),
    path('crearcliente/', views.crearcliente, name="crearcliente"),
    ]