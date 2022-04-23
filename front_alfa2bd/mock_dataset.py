import os
import django
from faker import Faker

fake = Faker()

from testdb.models import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'front_alfa2bd.settings')
django.setup()

# infraestrutura = InfraEstrutura(
#     inf_nome_cluster = 'test',
#     inf_nivel_gov = 1,
#     inf_nome_provedor = 'test',
# )

# infraestrutura.save()

# unidade_escolar = UnidadeEscolar(
#     uni_codigo_inep = 1234,
#     uni_nome = 'test',
#     uni_uf = 'RS',
#     uni_cep = '123',
#     uni_endereco = 'test',
#     uni_municipio = 'test',
#     uni_categ_admin = 2,
#     uni_depen_admin = 1,
# )

# unidade_escolar.save()
