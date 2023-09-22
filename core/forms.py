from django import forms


from .models import Livro


class LivroModelForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'estoque']


