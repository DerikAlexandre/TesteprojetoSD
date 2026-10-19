from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CadastroObjetoForm
from .models import CadastroDemonstracao


def index(request):
    if request.method == 'POST':
        form = CadastroObjetoForm(request.POST)
        if form.is_valid():
            form.salvar()
            messages.success(request, 'Objeto cadastrado com sucesso!')
            return redirect('enquetes:cadastro_objeto')
        messages.error(request, 'Não foi possível cadastrar. Corrija os campos indicados.')
    else:
        form = CadastroObjetoForm()
    return render(request, 'enquetes/cadastro_objeto.html', {'form': form})


def lista_objetos(request):
    objetos = CadastroDemonstracao.objects.order_by('-criado_em', '-id')
    return render(request, 'enquetes/lista_objetos.html', {'objetos': objetos})
