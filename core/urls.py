from django.urls import path
from core.views import index, cadastro, busca, resultadoBusca

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('busca/', busca, name='busca'),
    path('resultadobusca/', resultadoBusca, name='resultadoBusca')
]

