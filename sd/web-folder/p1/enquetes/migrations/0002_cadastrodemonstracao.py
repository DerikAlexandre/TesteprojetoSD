from django.db import migrations, models
import datetime


class Migration(migrations.Migration):
    dependencies = [('enquetes', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='CadastroDemonstracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=60)),
                ('contato', models.CharField(max_length=200)),
                ('categoria', models.CharField(choices=[('DOC', 'Documento'), ('ELE', 'Eletronicos'), ('ROU', 'Roupas'), ('ACE', 'Acessorios'), ('MAT', 'Materiais academicos')], max_length=3)),
                ('situacao', models.CharField(choices=[('ENC', 'Objeto encontrado'), ('PER', 'Objeto nao encontrado')], max_length=3)),
                ('nome_objeto', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=30)),
                ('criado_em', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
