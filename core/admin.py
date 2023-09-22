from django.contrib import admin
from .models import Livro


class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'estoque')


admin.site.register(Livro, LivroAdmin)
