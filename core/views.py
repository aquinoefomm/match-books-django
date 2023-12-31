from django.shortcuts import render
from .models import Livro
from django.contrib import messages

from .forms import LivroModelForm


def index(request):
    context = {
        'livros': Livro.objects.all()
    }
    return render(request, 'index.html', context)


def cadastro(request):
    if str(request.method) == 'POST':
        form = LivroModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações salvas com sucesso!')
        else:
            messages.error(request, 'Erro ao salvar informações!')
    else:
        form = LivroModelForm()
    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)


def busca(request):
    return render(request, 'busca.html')


def resultado_busca(request):
    context = {
        'livros_titulo': Livro.objects.filter(nome__icontains=request.GET['nome']),
        'livros_autor': Livro.objects.filter(autor__icontains=request.GET['autor'])
    }
    return render(request, 'resultbusca.html', context)







