from django.db import models

class Node(models.Model):
    nod_id = models.AutoField(primary_key=True, db_column='nod_id')
    inf_id = models.ForeignKey('InfraEstrutura', models.DO_NOTHING, db_column='inf_id')
    nod_ip = models.CharField(max_length=15, db_column='nod_ip')
    nod_porta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'NODE'