from django.shortcuts import render, redirect
from .models import Autor
from .forms import AutorForm


def autor(request):
    autores = Autor.objects.all()
    ctx = {
        'autores': autores,
    }
    return render(request, 'autor.html', ctx)


def createAutor(request):
    if request.method == 'GET':
        form = AutorForm()
        ctx = {
            'form': form
        }
    else:
        form = AutorForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('autor')

    return render(request, 'manage_autor.html', ctx)


def editAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'GET':
        form = AutorForm(instance= autor)
        ctx = {
            'form': form
        }
    else:
        form = AutorForm(request.POST, instance=autor)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('autor')
    return render(request, 'manage_autor.html', ctx)


def deleteAutor(request, id):
    autor = Autor.objects.get(id = id)
    autor.delete()
    return redirect('autor')