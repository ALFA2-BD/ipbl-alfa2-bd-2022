import os
import django
from faker import Faker
from random import randint, uniform, choices
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'front_alfa2bd.settings')
django.setup()

from testdb.models import *

def main():
    fake = Faker(locale='pt_BR')
    number_examples = 10

    for index in range(number_examples):
        infraestrutura = InfraEstrutura(
            inf_nome_cluster = fake.hostname(),
            inf_nivel_gov = randint(1, 3),
            inf_nome_provedor = fake.company(),
        )
        infraestrutura.save()

    for index in range(number_examples):
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
    
    for index in range(number_examples):
        name_student = fake.name().split()
        school_student = fake.name().split()
        aluno = Aluno(
            alu_primeiro_nome = name_student[0],
            alu_segundo_nome = name_student[1],
            alu_escola = "Escola " + school_student[0]
        )
        aluno.save()

    for index in range(number_examples):
        name_prof = fake.name().split()
        school_prof = fake.name().split()
        professor = Professor(
            pro_primeiro_nome = name_prof[0],
            pro_segundo_nome = name_prof[1],
            pro_escola = "Escola " + school_prof[0]
        )
        professor.save()

    alunos = list(Aluno.objects.all())
    professores = list(Professor.objects.all())
    
    for index in range(min(len(alunos), len(professores))):
        # grade 0 means not tested
        second_probability = 0.3
        second_grade = choices([0, uniform(0, 100)], [1-second_probability, second_probability])[0]
        
        if second_grade != 0:
            third_grade = 0
        else:
            third_probability = 0.1
            third_grade = choices([0, uniform(0, 100)], [1-third_probability, third_probability])[0]

        coleta = Coleta(
            alu_id = Aluno.objects.get(pk=alunos[index].alu_id),
            pro_id = Professor.objects.get(pk=professores[index].pro_id),
            col_prim_tentativa = uniform(0, 100),
            col_seg_tentativa = second_grade,
            col_ter_tentativa = third_grade,
        )
        coleta.save()

if __name__ == '__main__':
    main()
