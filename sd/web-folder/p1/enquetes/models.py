from django.db import models
from datetime import date

class PerfilUsuario(models.Model):
    class statusUser(models.TextChoices):
            # KEY = VALOR, TEXTO NA TELA
            ADMIN = 'ADM', 'Administrador'
            USUARIO = 'USU', 'Usuario'

    nome = models.CharField(max_length=60)
    criado_em = models.DateField(default=date.today)

    tipo_usuario = models.CharField(
        max_length=3,
        choices=statusUser.choices
    )

    informacoes_adicionais = models.CharField(max_length=200)

class Categoria(models.Model):

    class statusObject(models.TextChoices):
        DOCUMENTOS = 'DOC', 'Documento'
        ELETRONICOS = 'ELE', 'Eletronicos'
        ROUPAS = 'ROU', 'Roupas'
        ACESSORIOS = 'ACE', 'Acessorios'
        MATERIAIS_ACADEMICOS = 'MAT', 'Materiais academicos'

    classificacao_objeto = models.CharField(
        max_length=3,
        choices=statusObject.choices
    )

class Objeto_Perdido(models.Model):
    perfilusuario = models.ForeignKey(PerfilUsuario, models.CASCADE, related_name='objeto_perdido')
    categoria = models.ForeignKey(Categoria, models.PROTECT)

    class statusObjeto(models.TextChoices):
                ENCONTRADO = 'ENC', 'Objeto encontrado'
                PERDIDO = 'PER', 'Objeto nao encontrado'
    
    situacao_objeto = models.CharField(
         max_length=3,
         choices=statusObjeto.choices
    )

    nome = models.CharField(max_length=50)

    descricao = models.CharField(max_length=200)

    situacao_adicional = models.CharField(
         max_length=200,
         blank=True,
         null=True
    )

    criado_em = models.DateField(default=date.today)

    data_do_objetoPerdido = models.DateField(default=date.today)

class Local(models.Model):
    objeto_perdido = models.OneToOneField(Objeto_Perdido, models.CASCADE, 
                                          related_name='local', primary_key=True)

    class statusLocal(models.TextChoices):
            BLOCO_DE_AULAS = 'BDA', 'Bloco de aulas'
            BLOCO_DOS_COLEGIADOS = 'BDC', 'Bloco dos colegiados'
            BIBLIOTECA = 'BIB', 'Biblioteca'
            CANTINA = 'CAN', 'Cantina'

    local_bem_definido = models.CharField(
         max_length=3,
         choices=statusLocal.choices,
         blank=True,
         null=True 
    )

    sala = models.IntegerField(
         blank=True,
         null=True
    )

    outro_lugar = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    detalhes_adicionais = models.CharField(
         max_length=200,
         blank=True,
         null=True
    )

    data_quePerdeu = models.DateField(default=date.today)


class Publicacao(models.Model):
    # Protect
    objeto_perdido = models.ForeignKey(Objeto_Perdido, models.PROTECT, related_name='publicacao')

    publicacao = models.CharField(max_length=200)
    criado_em = models.DateField(default=date.today)
    

class Reivindicacao(models.Model):
    objeto_perdido = models.ForeignKey(Objeto_Perdido, models.CASCADE, related_name='reivindicacao')

    # nome = models.CharField(max_length=50)
    solicitacao_textual = models.CharField(max_length=200, blank=True, null=True)

class Notificacao(models.Model):
    titulo = models.CharField(max_length=200)
    criado_em = models.DateField(default=date.today)
    mensagem_lida = models.IntegerField(default=0)
    
class Mensagem(models.Model):
    perfilusuario = models.ForeignKey(PerfilUsuario, models.CASCADE, related_name='mensagem_recebedor')

    enviado_por =  models.OneToOneField(PerfilUsuario, models.PROTECT, 
                                          related_name='mensagem_enviada_por', primary_key=True)
    notificacao = models.ForeignKey(Notificacao, models.CASCADE, related_name='mensagem_para_enviar')
    
    criado_em = models.DateField(default=date.today)
    mensagem_lida = models.IntegerField(default=0)

    mensagem = models.CharField(max_length=200)


class CadastroDemonstracao(models.Model):
    """Registro usado pelo formulário público de demonstração."""
    nome_responsavel = models.CharField(max_length=60)
    contato = models.CharField(max_length=200)
    categoria = models.CharField(max_length=3, choices=Categoria.statusObject.choices)
    situacao = models.CharField(max_length=3, choices=Objeto_Perdido.statusObjeto.choices)
    nome_objeto = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    local = models.CharField(max_length=30)
    criado_em = models.DateField(default=date.today)

    def __str__(self):
        return self.nome_objeto
