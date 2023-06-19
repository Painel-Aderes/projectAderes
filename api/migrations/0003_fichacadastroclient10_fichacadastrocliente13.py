# Generated by Django 4.2.1 on 2023-06-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_fichacadastroclient10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichaCadastroClient10',
            fields=[
                ('idficha_cadastro_client_1_0', models.AutoField(db_column='idficha_cadastro_client_1.0', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(unique=True)),
                ('identidade', models.CharField(max_length=100, unique=True)),
                ('filiacao_mae', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=100)),
                ('cep', models.IntegerField()),
            ],
            options={
                'db_table': 'ficha_cadastro_client_1.0',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FichaCadastroCliente13',
            fields=[
                ('idficha_cadastro_cliente_1_3', models.AutoField(db_column='idficha_cadastro_cliente_1.3', primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=100)),
                ('cpnj', models.IntegerField(unique=True)),
                ('inscricao_estadual', models.CharField(max_length=100)),
                ('incricao_municipal', models.CharField(max_length=100)),
                ('data_abertura', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('setor', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('ijc', models.CharField(max_length=100)),
                ('endereco_comercial', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ficha_cadastro_cliente_1.3',
                'managed': False,
            },
        ),
    ]