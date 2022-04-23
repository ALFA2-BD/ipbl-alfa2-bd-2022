from django.db import models

class Contrato(models.Model):
    con_id = models.AutoField(primary_key=True, db_column='con_id')
    uni_id = models.ForeignKey('UndadeEscolar', models.DO_NOTHING, db_column='uni_id')
    inf_id = models.ForeignKey('InfraEstrutura', models.DO_NOTHING, db_column='inf_id')
    con_data_ini = models.DateField(db_column='con_data_ini')
    con_data_fim = models.DateField(db_column='con_data_fim')
    con_tipo = models.IntegerField(db_column='con_tipo')

    class Meta:
        managed = False
        db_table = 'CONTRATO'
