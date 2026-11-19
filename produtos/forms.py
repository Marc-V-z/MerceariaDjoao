from django import forms

from .models import Produto


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descrição', 'preço', 'validade']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }