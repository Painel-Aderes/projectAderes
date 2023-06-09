# Generated by Django 4.2.1 on 2023-05-31 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artesoes',
            fields=[
                ('idartesoes', models.AutoField(primary_key=True, serialize=False)),
                ('nome_social', models.CharField(max_length=100)),
                ('sicab', models.IntegerField(unique=True)),
                ('status_carteira', models.CharField(max_length=7)),
                ('status_cadastro', models.CharField(max_length=7)),
                ('data_cadastro', models.DateTimeField()),
                ('data_validade', models.DateTimeField()),
                ('tipo', models.CharField(max_length=15)),
                ('uf', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('codigo_municipio', models.IntegerField()),
            ],
            options={
                'db_table': 'artesoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
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
        migrations.CreateModel(
            name='JuntaComercial',
            fields=[
                ('idjunta_comercial', models.AutoField(primary_key=True, serialize=False)),
                ('nome_empresa', models.CharField(max_length=100)),
                ('porte', models.CharField(max_length=100)),
                ('mei', models.CharField(max_length=5)),
                ('cnpj', models.IntegerField(unique=True)),
                ('ds_logradouro', models.CharField(max_length=100)),
                ('ds_numero', models.CharField(max_length=100)),
                ('ds_complemento', models.CharField(max_length=100)),
                ('no_bairro', models.CharField(max_length=100)),
                ('nr_cep', models.CharField(max_length=100)),
                ('no_municipio', models.CharField(max_length=100)),
                ('ds_atividade', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'junta_comercial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Microcredito',
            fields=[
                ('idmicrocredito', models.AutoField(primary_key=True, serialize=False)),
                ('fonte_recursos', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('contratacao', models.CharField(max_length=100)),
                ('carencia', models.CharField(max_length=100)),
                ('quantos_prs', models.CharField(max_length=100)),
                ('valor_prs', models.CharField(max_length=100)),
                ('tac', models.CharField(max_length=100)),
                ('juros', models.CharField(max_length=100)),
                ('giro', models.CharField(max_length=100)),
                ('fixo', models.CharField(max_length=100)),
                ('valor_total', models.CharField(max_length=100)),
                ('atividade', models.CharField(max_length=100)),
                ('ano', models.CharField(max_length=100)),
                ('mes', models.CharField(max_length=100)),
                ('modalidade', models.CharField(max_length=100)),
                ('legislacao', models.CharField(max_length=100)),
                ('justificativa', models.CharField(max_length=100)),
                ('empresas_geradas', models.CharField(max_length=100)),
                ('empregos_gerados', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'microcredito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idmunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('concat_uf', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('ibge', models.CharField(max_length=100)),
                ('ibge7', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=100)),
                ('porte', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seger',
            fields=[
                ('idseger', models.AutoField(primary_key=True, serialize=False)),
                ('orgao', models.CharField(max_length=100)),
                ('processo', models.CharField(max_length=100)),
                ('processo_finalizado', models.CharField(max_length=5)),
                ('lote', models.CharField(max_length=100)),
                ('lote_excluisivo_me_epp', models.CharField(db_column='lote_excluisivo_me/epp', max_length=5)),
                ('modalidade', models.CharField(max_length=100)),
                ('data_apuracao', models.DateField()),
                ('cpf_cnpj', models.IntegerField(unique=True)),
                ('estado_fornecido', models.CharField(max_length=100)),
                ('natureza_fornecedor', models.CharField(max_length=100)),
                ('fornecedor_me_epp', models.CharField(db_column='fornecedor_me/epp', max_length=100)),
                ('valor_estimado_lote', models.IntegerField()),
                ('valor_apurado', models.IntegerField()),
            ],
            options={
                'db_table': 'seger',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtesoesHasMunicipio',
            fields=[
                ('artesoes_idartesoes', models.OneToOneField(db_column='artesoes_idartesoes', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.artesoes')),
            ],
            options={
                'db_table': 'artesoes_has_municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JuntaComercialHasMunicipio',
            fields=[
                ('junta_comercial_idjunta_comercial', models.OneToOneField(db_column='junta_comercial_idjunta_comercial', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.juntacomercial')),
            ],
            options={
                'db_table': 'junta_comercial_has_municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MicrocreditoHasMunicipio',
            fields=[
                ('microcredito_idmicrocredito', models.OneToOneField(db_column='microcredito_idmicrocredito', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.microcredito')),
            ],
            options={
                'db_table': 'microcredito_has_municipio',
                'managed': False,
            },
        ),
    ]
