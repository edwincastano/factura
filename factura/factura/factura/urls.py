"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import firtsView, index, index2
from core.views import autor, createAutor, editAutor, deleteAutor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firtsView),
    path('index/<int:agno>/<int:actual>/', index),
    path('index2/', index2),
    path('autor/', autor, name = 'autor'),
    path('createAutor/', createAutor, name = 'create_autor'),
    path('editAutor/<int:id>/', editAutor, name = 'edit_autor'),
    path('deleteAutor/<int:id>/', deleteAutor, name = 'delete_autor')
]
