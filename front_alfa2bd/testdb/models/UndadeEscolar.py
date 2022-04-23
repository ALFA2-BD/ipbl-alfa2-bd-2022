from django.db import models

class UndadeEscolar(models.Model):
    uni_id = models.AutoField(primary_key=True, db_column='uni_id')
    uni_codigo_inep = models.IntegerField(db_column='uni_codigo_inep')
    uni_nome = models.CharField(max_length=255, db_column='uni_nome')
    uni_uf = models.CharField(max_length=2, db_column='uni_uf')
    uni_cep = models.CharField(max_length=9, db_column='uni_cep')
    uni_endereco = models.CharField(max_length=255, db_column='uni_endereco')
    uni_municipio = models.CharField(max_length=50, db_column='uni_municipio')
    uni_categ_admin = models.IntegerField(db_column='uni_categ_admin')
    uni_depen_admin = models.IntegerField(db_column='uni_depen_admin')

    class Meta:
        managed = False
        db_table = 'UNIDADE_ESCOLAR'