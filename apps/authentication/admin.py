# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(InfraEstrutura)
admin.site.register(Node)
admin.site.register(UnidadeEscolar)
admin.site.register(Contrato)

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coleta)
