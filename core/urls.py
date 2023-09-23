from django.urls import path
from core.views import index, cadastro, busca, resultado_busca_titulo, resultado_busca_autor

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('busca/', busca, name='busca'),
    path('resultadobuscatitulo/', resultado_busca_titulo, name='resultadoBuscaTitulo'),
    path('resultadobuscaautor/', resultado_busca_autor, name='resultadoBuscaAutor')
]

