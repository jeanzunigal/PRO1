from django.contrib import admin
from django.urls import path, include
from cliente import views
urlpatterns = [
    path('cliente/', views.cliente, name="cliente"),
    path('crearcliente/', views.crearcliente, name="crearcliente"),
    path('modificarcliente/<int:pk>', views.modificarcliente, name="modificarcliente"),
    path('eliminarcliente/<int:pk>', views.eliminarcliente, name="eliminarcliente"),
    path('2mecanico/', views.mecanico, name="2mecanico"),
    path('2crearmecanico/', views.crearmecanico, name="2crearmecanico"),
]
