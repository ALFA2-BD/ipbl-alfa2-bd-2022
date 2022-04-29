# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Unidade_Escolar(models.Model):
    uni_id = models.AutoField()
    uni_codigo_inep = models.IntegerField()
    uni_nome = models.CharField(max_length=100)
    uni_uf = models.CharField(max_length=2)
    uni_cep = models.CharField(max_length=9)
    uni_endereco = models.CharField(max_length=255)
    uni_municipio = models.CharField(max_length=50)
    uni_categ_admin = models.IntegerField()
    uni_depen_admin = models.IntegerField()


class Infraestrutura(models.Model):
    inf_id = models.AutoField()
    inf_nome_cluster = models.CharField(max_length=30)
    inf_nivel_gov = models.IntegerField()
    inf_nome_provedor = models.CharField(max_length=255)
