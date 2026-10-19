from django.contrib import admin
from .models import (
    PerfilUsuario, Categoria, Objeto_Perdido, Local, CadastroDemonstracao,
    Publicacao, Reivindicacao, Notificacao, Mensagem
)

admin.site.register(CadastroDemonstracao)


class LocalInline(admin.StackedInline):
    model = Local
    extra = 0
    max_num = 1


class PublicacaoInline(admin.TabularInline):
    model = Publicacao
    extra = 0


class ReivindicacaoInline(admin.TabularInline):
    model = Reivindicacao
    extra = 0


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_usuario', 'criado_em')
    list_filter = ('tipo_usuario',)
    search_fields = ('nome', 'informacoes_adicionais')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'classificacao_objeto')
    list_filter = ('classificacao_objeto',)


@admin.register(Objeto_Perdido)
class ObjetoPerdidoAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'situacao_objeto', 'perfilusuario',
        'categoria', 'criado_em'
    )
    list_filter = ('situacao_objeto', 'categoria')
    search_fields = ('nome', 'descricao', 'perfilusuario__nome')
    inlines = [LocalInline, PublicacaoInline, ReivindicacaoInline]


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('objeto_perdido', 'local_bem_definido', 'sala')
    list_filter = ('local_bem_definido',)


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('objeto_perdido', 'publicacao', 'criado_em')
    search_fields = ('publicacao', 'objeto_perdido__nome')


@admin.register(Reivindicacao)
class ReivindicacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'objeto_perdido', 'solicitacao_textual')
    search_fields = ('solicitacao_textual', 'objeto_perdido__nome')


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado_em', 'mensagem_lida')
    list_filter = ('mensagem_lida',)
    search_fields = ('titulo',)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = (
        'enviado_por', 'perfilusuario', 'mensagem',
        'notificacao', 'criado_em', 'mensagem_lida'
    )
    list_filter = ('mensagem_lida',)
    search_fields = (
        'mensagem', 'perfilusuario__nome', 'enviado_por__nome'
    )
