# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artesoes(models.Model):
    idartesoes = models.AutoField(primary_key=True)  # The composite primary key (idartesoes, sicab) found, that is not supported. The first column is selected.
    nome_social = models.CharField(max_length=100)
    sicab = models.IntegerField(unique=True)
    status_carteira = models.CharField(max_length=7)
    status_cadastro = models.CharField(max_length=7)
    data_cadastro = models.DateField(blank=True, null=True)
    data_validade = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=15)
    uf = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    codigo_municipio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'artesoes'
        unique_together = (('idartesoes', 'sicab'),)


class ArtesoesHasMunicipio(models.Model):
    artesoes_idartesoes = models.OneToOneField(Artesoes, models.DO_NOTHING, db_column='artesoes_idartesoes', primary_key=True)  # The composite primary key (artesoes_idartesoes, artesoes_sicab, municipio_idmunicipio) found, that is not supported. The first column is selected.
    artesoes_sicab = models.ForeignKey(Artesoes, models.DO_NOTHING, db_column='artesoes_sicab', to_field='sicab', related_name='artesoeshasmunicipio_artesoes_sicab_set')
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_idmunicipio')

    class Meta:
        managed = False
        db_table = 'artesoes_has_municipio'
        unique_together = (('artesoes_idartesoes', 'artesoes_sicab', 'municipio_idmunicipio'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FichaCadastroClient10(models.Model):
    idficha_cadastro_client_1_0 = models.AutoField(db_column='idficha_cadastro_client_1.0', primary_key=True)  # Field renamed to remove unsuitable characters. The composite primary key (idficha_cadastro_client_1.0, cpf) found, that is not supported. The first column is selected.
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)
    identidade = models.CharField(unique=True, max_length=100)
    filiacao_mae = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    cep = models.IntegerField()
    ficha_cadastro_cliente_1_3_idficha_cadastro_cliente_1_3 = models.ForeignKey('FichaCadastroCliente13', models.DO_NOTHING, db_column='ficha_cadastro_cliente_1.3_idficha_cadastro_cliente_1.3')  # Field renamed to remove unsuitable characters.
    ficha_cadastro_cliente_1_3_cpnj = models.ForeignKey('FichaCadastroCliente13', models.DO_NOTHING, db_column='ficha_cadastro_cliente_1.3_cpnj', to_field='cpnj', related_name='fichacadastroclient10_ficha_cadastro_cliente_1_3_cpnj_set')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ficha_cadastro_client_1.0'
        unique_together = (('idficha_cadastro_client_1_0', 'cpf'),)


class FichaCadastroCliente13(models.Model):
    idficha_cadastro_cliente_1_3 = models.AutoField(db_column='idficha_cadastro_cliente_1.3', primary_key=True)  # Field renamed to remove unsuitable characters. The composite primary key (idficha_cadastro_cliente_1.3, cpnj) found, that is not supported. The first column is selected.
    razao_social = models.CharField(max_length=100)
    cpnj = models.IntegerField(unique=True)
    inscricao_estadual = models.CharField(max_length=100)
    incricao_municipal = models.CharField(max_length=100)
    data_abertura = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    ijc = models.CharField(max_length=100)
    endereco_comercial = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    ficha_cadastro_client_1_0_idficha_cadastro_client_1_0 = models.ForeignKey(FichaCadastroClient10, models.DO_NOTHING, db_column='ficha_cadastro_client_1.0_idficha_cadastro_client_1.0')  # Field renamed to remove unsuitable characters.
    ficha_cadastro_client_1_0_cpf = models.ForeignKey(FichaCadastroClient10, models.DO_NOTHING, db_column='ficha_cadastro_client_1.0_cpf', to_field='cpf', related_name='fichacadastrocliente13_ficha_cadastro_client_1_0_cpf_set')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ficha_cadastro_cliente_1.3'
        unique_together = (('idficha_cadastro_cliente_1_3', 'cpnj'),)


class JuntaComercial(models.Model):
    idjunta_comercial = models.AutoField(primary_key=True)  # The composite primary key (idjunta_comercial, cnpj) found, that is not supported. The first column is selected.
    nome_empresa = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    mei = models.CharField(max_length=5)
    cnpj = models.IntegerField(unique=True)
    ds_logradouro = models.CharField(max_length=100)
    ds_numero = models.CharField(max_length=100)
    ds_complemento = models.CharField(max_length=100)
    no_bairro = models.CharField(max_length=100)
    nr_cep = models.CharField(max_length=100)
    no_municipio = models.CharField(max_length=100)
    ds_atividade = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'junta_comercial'
        unique_together = (('idjunta_comercial', 'cnpj'),)


class JuntaComercialHasMunicipio(models.Model):
    junta_comercial_idjunta_comercial = models.OneToOneField(JuntaComercial, models.DO_NOTHING, db_column='junta_comercial_idjunta_comercial', primary_key=True)  # The composite primary key (junta_comercial_idjunta_comercial, junta_comercial_cnpj, municipio_idmunicipio) found, that is not supported. The first column is selected.
    junta_comercial_cnpj = models.ForeignKey(JuntaComercial, models.DO_NOTHING, db_column='junta_comercial_cnpj', to_field='cnpj', related_name='juntacomercialhasmunicipio_junta_comercial_cnpj_set')
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_idmunicipio')

    class Meta:
        managed = False
        db_table = 'junta_comercial_has_municipio'
        unique_together = (('junta_comercial_idjunta_comercial', 'junta_comercial_cnpj', 'municipio_idmunicipio'),)


class Microcredito(models.Model):
    idmicrocredito = models.AutoField(primary_key=True)
    fonte_recursos = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    contratacao = models.CharField(max_length=100)
    carencia = models.CharField(max_length=100)
    quantos_prs = models.CharField(max_length=100)
    valor_prs = models.CharField(max_length=100)
    tac = models.CharField(max_length=100)
    juros = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)
    fixo = models.CharField(max_length=100)
    valor_total = models.CharField(max_length=100)
    atividade = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    mes = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100)
    legislacao = models.CharField(max_length=100)
    justificativa = models.CharField(max_length=100)
    empresas_geradas = models.CharField(max_length=100)
    empregos_gerados = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'microcredito'


class MicrocreditoHasMunicipio(models.Model):
    microcredito_idmicrocredito = models.OneToOneField(Microcredito, models.DO_NOTHING, db_column='microcredito_idmicrocredito', primary_key=True)  # The composite primary key (microcredito_idmicrocredito, municipio_idmunicipio) found, that is not supported. The first column is selected.
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_idmunicipio')

    class Meta:
        managed = False
        db_table = 'microcredito_has_municipio'
        unique_together = (('microcredito_idmicrocredito', 'municipio_idmunicipio'),)


class Municipio(models.Model):
    idmunicipio = models.AutoField(primary_key=True)
    concat_uf = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    ibge = models.CharField(max_length=100)
    ibge7 = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'municipio'


class Seger(models.Model):
    idseger = models.AutoField(primary_key=True)  # The composite primary key (idseger, cpf_cnpj) found, that is not supported. The first column is selected.
    orgao = models.CharField(max_length=100)
    processo = models.CharField(max_length=100)
    processo_finalizado = models.CharField(max_length=5)
    lote = models.CharField(max_length=100)
    lote_excluisivo_me_epp = models.CharField(db_column='lote_excluisivo_me/epp', max_length=5)  # Field renamed to remove unsuitable characters.
    modalidade = models.CharField(max_length=100)
    data_apuracao = models.DateField()
    cpf_cnpj = models.IntegerField(unique=True)
    estado_fornecido = models.CharField(max_length=100)
    natureza_fornecedor = models.CharField(max_length=100)
    fornecedor_me_epp = models.CharField(db_column='fornecedor_me/epp', max_length=100)  # Field renamed to remove unsuitable characters.
    valor_estimado_lote = models.IntegerField()
    valor_apurado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seger'
        unique_together = (('idseger', 'cpf_cnpj'),)
