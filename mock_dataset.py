### Fake (PT BR) DOC: https://faker.readthedocs.io/en/master/locales/pt_BR.html ###
from faker import Faker
from random import randint, uniform, choices
from datetime import datetime, timedelta
from dataset.ScriptsMongoDB import ScriptsMongoDB
from pymongo import InsertOne

def main(*args, **kwargs):

    locate = 'pt_BR' if 'locate' not in kwargs else kwargs['locate']
    number_of_examples = 10 if 'number_of_examples' not in kwargs else kwargs['number_of_examples']
    delete_elements_before = False if 'delete_elements_before' not in kwargs else kwargs['delete_elements_before']

    fake = Faker(locale=locate)

    scripts_mongodb = ScriptsMongoDB()

    ### Fake Frases ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='frases')

    if scripts_mongodb.number_elements_collection(collection_name='frases') == 0:

        obj_frases = []

        for i in range(number_of_examples):
            json_frase = {
                'frase': fake.catch_phrase(),
                'tipo': randint(1, 3)
            }
            obj_frases.append(InsertOne(json_frase))

        collection_frases = scripts_mongodb.db['frases']

        collection_frases.bulk_write(obj_frases)

### Fake Avaliacoes ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='avaliacoes')

    if scripts_mongodb.number_elements_collection(collection_name='avaliacoes') == 0:

        obj_avaliacoes = []
        frases = scripts_mongodb.get_collection_data(collection_name = 'frases')
        # TODO: add aluno, prof and audios
        for i in range(number_of_examples):

            json_avaliacoes = {
                'avaliacoes':[
                    {
                        'data':fake.date(),
                        'coleta': [
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            },
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            },
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            }
                        ]
                    },
                    {
                        'data':fake.date(),
                        'coleta': [
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            },
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            },
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            }
                        ]
                    },
                    {
                        'data':fake.date(),
                        'coleta': [
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            },
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            },
                            {
                                'audio': None,
                                'metrica': uniform(0,10),
                                'frase': frases[randint(0,number_of_examples-1)]
                            }
                        ]
                    }
                ],
                'aluno': None,
                'professor' : None
            }
            obj_avaliacoes.append(InsertOne(json_avaliacoes))

        collection_avaliacoes = scripts_mongodb.db['avaliacoes']

        collection_avaliacoes.bulk_write(obj_avaliacoes)

### Fake Professores ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='professores')

    if scripts_mongodb.number_elements_collection(collection_name='professores') == 0:

        obj_professores = []
        # TODO: add turma
        for i in range(number_of_examples - 1):

            json_professores = {
                'nome': fake.first_name(),
                'sobrenome': fake.last_name(),
                'hash_senha' : 1234,
                'turma' : None
            }
            obj_professores.append(InsertOne(json_professores))

        collection_professores = scripts_mongodb.db['professores']

        collection_professores.bulk_write(obj_professores)

### Fake Alunos ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='alunos')

    if scripts_mongodb.number_elements_collection(collection_name='alunos') == 0:

        obj_alunos = []
        avaliacoes = scripts_mongodb.get_collection_data(collection_name = 'avaliacoes')
        # TODO: add turma
        for i in range(number_of_examples):

            json_alunos = {
                'nome': fake.first_name(),
                'sobrenome': fake.last_name(),
                'tipo': randint(1,3),
                'avaliacao' : avaliacoes[i],
                'turma' : None
            }
            obj_alunos.append(InsertOne(json_alunos))

        collection_alunos = scripts_mongodb.db['alunos']

        collection_alunos.bulk_write(obj_alunos)


### Fake Turmas ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='turmas')

    if scripts_mongodb.number_elements_collection(collection_name='turmas') == 0:

        obj_turmas = []
        alunos = scripts_mongodb.get_collection_data(collection_name = 'alunos')
        profs = scripts_mongodb.get_collection_data(collection_name = 'professores')

        for i in range(number_of_examples - 1):

            json_turmas = {
                'ano': randint(2022, 2025),
                'ano_escolar': randint(1,6),
                'nome_provedor': fake.name(),
                'alunos' : [
                    alunos[i],
                    alunos[i+1]
                ],
                'professor' : profs[i]
            }
            obj_turmas.append(InsertOne(json_turmas))

        collection_turmas = scripts_mongodb.db['turmas']

        collection_turmas.bulk_write(obj_turmas)

### Fake Infraestruturas ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='infraestruturas')

    if scripts_mongodb.number_elements_collection(collection_name='infraestruturas') == 0:

        obj_infras = []
        #TODO: ADD escolas (many to many)

        for i in range(number_of_examples):

            json_infras = {
                'nome': fake.cryptocurrency_code(),
                'nvl_gov': randint(1,3),
                'nome_provedor': fake.name(),
                'node' : [
                    {
                        'ip': fake.ipv4(),
                        'port': fake.port_number(is_system = True)
                    },
                    {
                        'ip': fake.ipv4(),
                        'port': fake.port_number(is_system = True)
                    }
                ],
                'escolas' : []
            }
            obj_infras.append(InsertOne(json_infras))

        collection_infras = scripts_mongodb.db['infraestruturas']

        collection_infras.bulk_write(obj_infras)


    ### Fake Escolas ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='escolas')

    if scripts_mongodb.number_elements_collection(collection_name='escolas') == 0:

        obj_escolas = []
        infras = scripts_mongodb.get_collection_data(collection_name = 'infraestruturas')
        turmas = scripts_mongodb.get_collection_data(collection_name = 'turmas')

        for i in range(number_of_examples - 2):

            json_escola = {
                'codigo_inep' : randint(10000000, 99999999),
                'nome': 'Escola' + fake.last_name(),
                'uf': fake.estado()[0],
                'cep': fake.postcode(False),
                'endereco': fake.address(),
                'municipio': fake.city(),
                'hash_senha': 1234,
                'categ_admin': randint(1,2),
                'depen_admin': randint(1,3),
                'infraestruturas' : [
                    infras[i],
                    infras[i+1]
                ],
                'turmas' : [
                    turmas[i],
                    turmas[i+1]
                ]
            }
            obj_escolas.append(InsertOne(json_escola))

        collection_escolas = scripts_mongodb.db['escolas']

        collection_escolas.bulk_write(obj_escolas)


    ### Fake Gestores ###

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='gestores')

    if scripts_mongodb.number_elements_collection(collection_name='gestores') == 0:

        obj_gestores = []
        escolas = scripts_mongodb.get_collection_data(collection_name = 'escolas')
        for i in range(number_of_examples - 3):

            json_gestor = {
                'nome': fake.first_name(),
                'sobrenome': fake.last_name(),
                'identificador': fake.cpf(),
                'hash_senha' : 1234,
                'escolas' : [
                    escolas[i],
                    escolas[i+1]
                ]
            }

            obj_gestores.append(InsertOne(json_gestor))

        collection_gestores = scripts_mongodb.db['gestores']

        collection_gestores.bulk_write(obj_gestores)

    ### Fake Gestores Admin

    if delete_elements_before:
        scripts_mongodb.delete_elements_from_collection(collection_name='gestor_admin')

    if scripts_mongodb.number_elements_collection(collection_name='gestor_admin') == 0:
        obj_gestores_admin = []
        gestores = scripts_mongodb.get_collection_data(collection_name = 'gestores')
        for i in range(number_of_examples - 4):
            json_gestor_admin = {
                'nome': fake.first_name(),
                'sobrenome' : fake.last_name(),
                'gestor_escola' : [
                    gestores[i],
                    gestores[i+1]
                ],
                'hash_senha' : 1234
            }
            obj_gestores_admin.append(InsertOne(json_gestor_admin))
        collection_gestores_admin = scripts_mongodb.db['gestores_admin']

        collection_gestores_admin.bulk_write(obj_gestores_admin)

if __name__ == '__main__':

    config = {
        'number_of_examples': 10,
        'locate': 'pt_BR',
        'delete_elements_before': True
    }

    main(**config)
