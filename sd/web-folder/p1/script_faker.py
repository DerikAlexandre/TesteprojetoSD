import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto1.settings')
django.setup()

from enquetes.models import (
    PerfilUsuario, Objeto_Perdido, Categoria, 
    Local, Publicacao, Reivindicacao, Mensagem, Notificacao
)

fake = Faker('pt_BR')

def popular_banco():
    print("Gerando centenas de registos falsos...")

    perfis = []
    for i in range(30):
        tipo = 'ADM' if i == 0 else 'USU'
        perfil = PerfilUsuario.objects.create(
            informacoes_adicionais=fake.sentence(),
            tipo_usuario=tipo
        )
        perfis.append(perfil)

    for _ in range(100):
        situacao = random.choice(['ENC', 'PER'])
        objeto = Objeto_Perdido.objects.create(
            situacao_objeto=situacao,
            nome=fake.word().capitalize(),
            descricao=fake.text(max_nb_chars=100),
            situacao_adicional=fake.sentence()
        )

        Categoria.objects.create(
            Objeto_Perdido=objeto,
            classificacao_objeto=random.choice(['DOC', 'ELE', 'ROU', 'ACE', 'MAT'])
        )

        Local.objects.create(
            Objeto_Perdido=objeto,
            local_bem_definido=random.choice(['BDA', 'BDC', 'BIB', 'CAN']),
            sala=random.randint(1, 50),
            outro_lugar=fake.word(),
            detalhes_adicionais=fake.sentence()
        )

        Publicacao.objects.create(
            Objeto_Perdido=objeto,
            publicacao=fake.sentence()
        )

        if random.choice([True, False]):
            Reivindicacao.objects.create(
                PerfilUsuario=random.choice(perfis),
                Objeto_Perdido=objeto,
                nome=fake.name(),
                solicitacao_textual=fake.sentence()
            )

    for perfil in perfis:
        for _ in range(3):
            Mensagem.objects.create(
                PerfilUsuario=perfil,
                mensagem=fake.sentence()
            )
            Notificacao.objects.create(
                PerfilUsuario=perfil
            )

    print("Sucesso! Base de dados populada com centenas de registos.")

if __name__ == '__main__':
    popular_banco()