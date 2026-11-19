from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistroForm
from .models import Produto


# Create your views here.

def produto_new(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produto_new')
    else:
        form = RegistroForm()
    return render(request, 'produtos/registro_form.html', {'form': form})


def produto_list(request):
    produtos = Produto.objects.order_by('nome')
    return render(request, 'produtos/list.html', {'produtos': produtos})