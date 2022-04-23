import os
import django
from faker import Faker
from random import randint
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'front_alfa2bd.settings')
django.setup()

from testdb.models import *

def main():
    fake = Faker(locale='pt_BR')

    for index in range(1000):
        infraestrutura = InfraEstrutura(
            inf_nome_cluster = fake.hostname(),
            inf_nivel_gov = randint(1, 3),
            inf_nome_provedor = fake.company(),
        )
        infraestrutura.save()

    for index in range(1000):
        unidade_escolar = UnidadeEscolar(
            uni_codigo_inep = randint(10000000,99999999),
            uni_nome = 'Escola ' + fake.bairro(),
            uni_uf = fake.estado_sigla(),
            uni_cep = fake.postcode(),
            uni_endereco = fake.street_address() ,
            uni_municipio = fake.administrative_unit(),
            uni_categ_admin = randint(1, 2),
            uni_depen_admin = randint(1, 4),
        )
        unidade_escolar.save()

    infraestruturas = list(InfraEstrutura.objects.all())
    unidades_escolares = list(UnidadeEscolar.objects.all())

    for index in range(len(infraestruturas)):
        node = Node(
            inf_id = InfraEstrutura.objects.get(pk=infraestruturas[index].inf_id),
            nod_ip = fake.ipv4(),
            nod_porta = randint(1,9999)
        )
        node.save()

    for index in range(min(len(infraestruturas), len(unidades_escolares))):
        date_init = datetime.now() - timedelta(days=randint(1, 300))
        data_fim = date_init + timedelta(days=randint(1, 300))

        contrato = Contrato(
            uni_id = UnidadeEscolar.objects.get(pk=unidades_escolares[index].uni_id),
            inf_id = InfraEstrutura.objects.get(pk=infraestruturas[index].inf_id),
            con_data_ini = date_init,
            con_data_fim = data_fim,
            con_tipo = randint(1, 3),
        )
        contrato.save()

if __name__ == '__main__':
    main()
