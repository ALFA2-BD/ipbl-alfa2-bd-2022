from django.db import models

class InfraEstrutura(models.Model):
    inf_id = models.AutoField(primary_key=True, db_column='inf_id')
    inf_nome_cluster = models.CharField(max_length=30, db_column='inf_nome_cluster')
    inf_nivel_gov = models.IntegerField(db_column='inf_nivel_gov')
    inf_nome_provedor = models.CharField(max_length=255, db_column='inf_nome_provedor')

    class Meta:
        managed = False
        db_table = 'INFRAESTRUTURA'