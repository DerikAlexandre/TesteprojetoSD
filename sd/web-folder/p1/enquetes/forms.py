from django import forms
from .models import CadastroDemonstracao, Categoria, Objeto_Perdido


class CadastroObjetoForm(forms.Form):
    nome_responsavel = forms.CharField(label='Seu nome', max_length=60)
    contato = forms.CharField(
        label='Contato ou informação adicional', max_length=200
    )
    categoria = forms.ChoiceField(
        label='Categoria', choices=Categoria.statusObject.choices
    )
    situacao = forms.ChoiceField(
        label='Situação', choices=Objeto_Perdido.statusObjeto.choices
    )
    nome_objeto = forms.CharField(label='Nome do objeto', max_length=50)
    descricao = forms.CharField(
        label='Descrição', max_length=200, widget=forms.Textarea(attrs={'rows': 4})
    )
    local = forms.CharField(label='Local', max_length=30)

    def clean_nome_responsavel(self):
        nome = self.cleaned_data['nome_responsavel'].strip()
        if not nome:
            raise forms.ValidationError('Informe seu nome.')
        return nome

    def clean_descricao(self):
        descricao = self.cleaned_data['descricao'].strip()
        if len(descricao) < 10:
            raise forms.ValidationError('A descrição deve ter pelo menos 10 caracteres.')
        return descricao

    def clean_local(self):
        local = self.cleaned_data['local'].strip()
        if not local:
            raise forms.ValidationError('Informe onde o objeto foi perdido ou encontrado.')
        return local

    def salvar(self):
        return CadastroDemonstracao.objects.create(
            nome_responsavel=self.cleaned_data['nome_responsavel'],
            contato=self.cleaned_data['contato'],
            categoria=self.cleaned_data['categoria'],
            situacao=self.cleaned_data['situacao'],
            nome_objeto=self.cleaned_data['nome_objeto'].strip(),
            descricao=self.cleaned_data['descricao'],
            local=self.cleaned_data['local'],
        )
