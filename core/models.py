from django.db import models


class Livro(models.Model):
    nome = models.CharField('Nome', max_length=100)
    autor = models.CharField('Autor', max_length=50)
    estoque = models.IntegerField('Estoque')
