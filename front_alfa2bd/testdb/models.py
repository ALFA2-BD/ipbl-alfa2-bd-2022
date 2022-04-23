from django.db import models
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'front_alfa2bd.settings')
django.setup()

class UnidadeEscolar(models.Model):
    uni_id = models.AutoField(primary_key=True, db_column='uni_id')
    uni_codigo_inep = models.IntegerField(db_column='uni_codigo_inep')
    uni_nome = models.CharField(db_column='uni_nome', max_length=255)
    uni_uf = models.CharField(db_column='uni_uf', max_length=2)
    uni_cep = models.CharField(db_column='uni_cep', max_length=9)
    uni_endereco = models.CharField(db_column='uni_endereco', max_length=255)
    uni_municipio = models.CharField(db_column='uni_municipio', max_length=50)
    uni_categ_admin = models.IntegerField(db_column='uni_categ_admin')
    uni_depen_admin = models.IntegerField(db_column='uni_depen_admin')

    class Meta:
        managed = False
        db_table = 'unidade_escolar'


class InfraEstrutura(models.Model):
    inf_id = models.AutoField(primary_key=True, db_column='inf_id')
    inf_nome_cluster = models.CharField(max_length=30, db_column='inf_nome_cluster')
    inf_nivel_gov = models.IntegerField(db_column='inf_nivel_gov')
    inf_nome_provedor = models.CharField(max_length=255, db_column='inf_nome_provedor')

    class Meta:
        managed = False
        db_table = 'infraestrutura'

class Contrato(models.Model):
    con_id = models.AutoField(primary_key=True, db_column='con_id')
    uni_id = models.ForeignKey(UnidadeEscolar, models.DO_NOTHING, db_column='uni_id')
    inf_id = models.ForeignKey(InfraEstrutura, models.DO_NOTHING, db_column='inf_id')
    con_data_ini = models.DateField(db_column='con_data_ini')
    con_data_fim = models.DateField(db_column='con_data_fim')
    con_tipo = models.IntegerField(db_column='con_tipo')

    class Meta:
        managed = False
        db_table = 'contrato'

class Node(models.Model):
    nod_id = models.AutoField(primary_key=True, db_column='nod_id')
    inf_id = models.ForeignKey(InfraEstrutura, models.DO_NOTHING, db_column='inf_id')
    nod_ip = models.CharField(max_length=15, db_column='nod_ip')
    nod_porta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node'
