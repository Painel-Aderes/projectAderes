# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artesoes(models.Model):
    idartesoes = models.AutoField(primary_key=True)  # The composite primary key (idartesoes, sicab, junta_comercial_idjunta_comercial, junta_comercial_cnpj) found, that is not supported. The first column is selected.
    nome_social = models.CharField(unique=True, max_length=45)
    sicab = models.CharField(unique=True, max_length=1)
    status_carteira = models.CharField(max_length=7)
    status_cadastro = models.CharField(max_length=7)
    data_cadastro = models.DateField()
    data_validade = models.DateField()
    tipo = models.CharField(max_length=15)
    uf = models.CharField(max_length=45)
    municipio = models.CharField(max_length=45)
    codigo_municipio = models.IntegerField()
    junta_comercial_idjunta_comercial = models.ForeignKey('JuntaComercial', models.DO_NOTHING, db_column='junta_comercial_idjunta_comercial')
    junta_comercial_cnpj = models.ForeignKey('JuntaComercial', models.DO_NOTHING, db_column='junta_comercial_cnpj', to_field='cnpj', related_name='artesoes_junta_comercial_cnpj_set')

    class Meta:
        managed = False
        db_table = 'artesoes'
        unique_together = (('idartesoes', 'sicab', 'junta_comercial_idjunta_comercial', 'junta_comercial_cnpj'),)


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
    razao_social = models.CharField(max_length=45)
    cpnj = models.IntegerField(unique=True)
    inscricao_estadual = models.CharField(max_length=45)
    incricao_municipal = models.CharField(max_length=45)
    data_abertura = models.CharField(max_length=45)
    nome_fantasia = models.CharField(max_length=45)
    setor = models.CharField(max_length=45)
    local = models.CharField(max_length=45)
    ijc = models.CharField(max_length=45)
    endereco_comercial = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    ficha_cadastro_client_1_0_idficha_cadastro_client_1_0 = models.ForeignKey(FichaCadastroClient10, models.DO_NOTHING, db_column='ficha_cadastro_client_1.0_idficha_cadastro_client_1.0')  # Field renamed to remove unsuitable characters.
    ficha_cadastro_client_1_0_cpf = models.ForeignKey(FichaCadastroClient10, models.DO_NOTHING, db_column='ficha_cadastro_client_1.0_cpf', to_field='cpf', related_name='fichacadastrocliente13_ficha_cadastro_client_1_0_cpf_set')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ficha_cadastro_cliente_1.3'
        unique_together = (('idficha_cadastro_cliente_1_3', 'cpnj'),)


class JuntaComercial(models.Model):
    idjunta_comercial = models.AutoField(primary_key=True)  # The composite primary key (idjunta_comercial, cnpj, artesoes_idartesoes, artesoes_sicab, artesoes_junta_comercial_idjunta_comercial, artesoes_junta_comercial_cnpj) found, that is not supported. The first column is selected.
    nome_empresa = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    mei = models.CharField(max_length=5)
    cnpj = models.IntegerField()
    ds_logradouro = models.CharField(max_length=100)
    ds_numero = models.CharField(max_length=100)
    ds_complemento = models.CharField(max_length=100)
    no_bairro = models.CharField(max_length=100)
    nr_cep = models.CharField(max_length=100)
    no_municipio = models.CharField(max_length=100)
    ds_atividade = models.CharField(max_length=100)
    artesoes_idartesoes = models.ForeignKey(Artesoes, models.DO_NOTHING, db_column='artesoes_idartesoes')
    artesoes_sicab = models.ForeignKey(Artesoes, models.DO_NOTHING, db_column='artesoes_sicab', to_field='sicab', related_name='juntacomercial_artesoes_sicab_set')
    artesoes_junta_comercial_idjunta_comercial = models.ForeignKey(Artesoes, models.DO_NOTHING, db_column='artesoes_junta_comercial_idjunta_comercial', to_field='junta_comercial_idjunta_comercial', related_name='juntacomercial_artesoes_junta_comercial_idjunta_comercial_set')
    artesoes_junta_comercial_cnpj = models.ForeignKey(Artesoes, models.DO_NOTHING, db_column='artesoes_junta_comercial_cnpj', to_field='junta_comercial_cnpj', related_name='juntacomercial_artesoes_junta_comercial_cnpj_set')

    class Meta:
        managed = False
        db_table = 'junta_comercial'
        unique_together = (('idjunta_comercial', 'cnpj', 'artesoes_idartesoes', 'artesoes_sicab', 'artesoes_junta_comercial_idjunta_comercial', 'artesoes_junta_comercial_cnpj'),)


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


class Municipio(models.Model):
    idmunicipio = models.AutoField(primary_key=True)
    concat_uf = models.CharField(max_length=45)
    municipio = models.CharField(max_length=45)
    ibge = models.CharField(max_length=45)
    ibge7 = models.CharField(max_length=45)
    uf = models.CharField(max_length=45)
    porte = models.CharField(max_length=45)
    capital = models.CharField(max_length=45)

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
