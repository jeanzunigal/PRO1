from django.contrib import admin
from django.urls import path, include

from usuarios import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]