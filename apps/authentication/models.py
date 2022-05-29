from django.db import models

# Create your models here.

# class UnidadeEscolar(models.Model):
#     uni_id = models.AutoField(primary_key=True, db_column='uni_id')
#     uni_codigo_inep = models.IntegerField(db_column='uni_codigo_inep')
#     uni_nome = models.CharField(db_column='uni_nome', max_length=255)
#     uni_uf = models.CharField(db_column='uni_uf', max_length=2)
#     uni_cep = models.CharField(db_column='uni_cep', max_length=9)
#     uni_endereco = models.CharField(db_column='uni_endereco', max_length=255)
#     uni_municipio = models.CharField(db_column='uni_municipio', max_length=50)
#     uni_categ_admin = models.IntegerField(db_column='uni_categ_admin')
#     uni_depen_admin = models.IntegerField(db_column='uni_depen_admin')

#     class Meta:
#         managed = False
#         db_table = 'unidade_escolar'


# class InfraEstrutura(models.Model):
#     inf_id = models.AutoField(primary_key=True, db_column='inf_id')
#     inf_nome_cluster = models.CharField(max_length=30, db_column='inf_nome_cluster')
#     inf_nivel_gov = models.IntegerField(db_column='inf_nivel_gov')
#     inf_nome_provedor = models.CharField(max_length=255, db_column='inf_nome_provedor')

#     class Meta:
#         managed = False
#         db_table = 'infraestrutura'

# class Contrato(models.Model):
#     con_id = models.AutoField(primary_key=True, db_column='con_id')
#     uni_id = models.ForeignKey(UnidadeEscolar, models.DO_NOTHING, db_column='uni_id')
#     inf_id = models.ForeignKey(InfraEstrutura, models.DO_NOTHING, db_column='inf_id')
#     con_data_ini = models.DateField(db_column='con_data_ini')
#     con_data_fim = models.DateField(db_column='con_data_fim')
#     con_tipo = models.IntegerField(db_column='con_tipo')

#     class Meta:
#         managed = False
#         db_table = 'contrato'

# class Node(models.Model):
#     nod_id = models.AutoField(primary_key=True, db_column='nod_id')
#     inf_id = models.ForeignKey(InfraEstrutura, models.DO_NOTHING, db_column='inf_id')
#     nod_ip = models.CharField(max_length=15, db_column='nod_ip')
#     nod_porta = models.IntegerField(db_column='nod_porta')

#     class Meta:
#         managed = False
#         db_table = 'node'

# class Aluno(models.Model):
#     alu_id = models.AutoField(primary_key=True, db_column='alu_id')
#     alu_primeiro_nome = models.CharField(db_column='alu_primeiro_nome', max_length=255)
#     alu_segundo_nome = models.CharField(db_column='alu_segundo_nome', max_length=255)
#     alu_escola = models.CharField(db_column='alu_escola', max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'aluno'

# class Professor(models.Model):
#     pro_id = models.AutoField(primary_key=True, db_column='pro_id')
#     pro_primeiro_nome = models.CharField(db_column='pro_primeiro_nome', max_length=255)
#     pro_segundo_nome = models.CharField(db_column='pro_segundo_nome', max_length=255)
#     pro_escola = models.CharField(db_column='pro_escola', max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'professor'

# class Coleta(models.Model):
#     col_id = models.AutoField(primary_key=True, db_column='col_id')
#     col_prim_tentativa = models.IntegerField(db_column='col_prim_tentativa')
#     col_seg_tentativa = models.IntegerField(db_column='col_seg_tentativa')
#     col_ter_tentativa = models.IntegerField(db_column='col_ter_tentativa')
#     alu_id = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='alu_id')
#     pro_id = models.ForeignKey(Professor, models.DO_NOTHING, db_column='pro_id')

#     class Meta:
#         managed = False
#         db_table = 'coleta'