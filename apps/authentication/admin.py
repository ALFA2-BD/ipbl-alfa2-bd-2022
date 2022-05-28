# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from tabnanny import verbose
from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(InfraEstrutura)
class AdminViewInfraEstrutura(admin.ModelAdmin):
    search_fields = [
        'inf_nome_provedor',
        'inf_nivel_gov',
        'inf_nome_cluster',
    ]
    list_display = [
        'inf_nome_provedor',
        'inf_nivel_gov',
        'inf_nome_cluster',
    ]

admin.site.register(Node)
admin.site.register(UnidadeEscolar)
admin.site.register(Contrato)

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coleta)
