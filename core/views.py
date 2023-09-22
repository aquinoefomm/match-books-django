from django.shortcuts import render
from .models import Livro

def index(request):
    context = {
        'livros': Livro.objects.all()
    }
    print(context['livros'])
    return render(request, 'index.html', context)


def cadastro(request):
    return render(request, 'cadastro.html')


def busca(request):
    return render(request, 'busca.html')

