### Fake (PT BR) DOC: https://faker.readthedocs.io/en/master/locales/pt_BR.html ###
from faker import Faker
from random import randint, uniform, choices
from datetime import datetime, timedelta
from dataset.ScriptsMongoDB import ScriptsMongoDB
from pymongo import InsertOne

def main(*args, **kwargs):

    locate = 'pt_BR' if 'locate' not in kwargs else kwargs['locate']
    number_of_examples = 10 if 'number_of_examples' not in kwargs else kwargs['number_of_examples']

    fake = Faker(locale=locate)

    scripts_mongodb = ScriptsMongoDB()

    ### Fake Frases ###

    if scripts_mongodb.number_elements_collection(collection_name='frases') == 0:

        obj_frases = []

        for _ in range(number_of_examples):
            json_frase = {
                'frase': fake.catch_phrase(),
                'tipo': randint(1, 3)
            }
            obj_frases.append(InsertOne(json_frase))

        collection_frases = scripts_mongodb.db['frases']

        collection_frases.bulk_write(obj_frases)

    ### Fake Professor ###

    if scripts_mongodb.number_elements_collection(collection_name='professores') == 0:

        obj_professores = []

        for _ in range(number_of_examples):
            json_professores = {
                'nome': {
                    'pnome': fake.first_name(),
                    'snome': fake.last_name()
                },
                'escola': 'Escola ' + fake.bairro(),
            }

            obj_turmas = []

            for _ in range(randint(1, number_of_examples)):
                json_turmas = {
                    'ano': randint(2000, 2040),
                    'ano_escolar': randint(1,9),
                }

                obj_alunos = []

                for _ in range(randint(1, number_of_examples)):
                    json_aluno = {
                        'nome': {
                            'pnome': fake.first_name(),
                            'snome': fake.last_name()
                        },
                        'idade': randint(7, 12)
                    }
                    obj_alunos.append(json_aluno)

                json_turmas['alunos'] = obj_alunos

                obj_turmas.append(json_turmas)

            json_professores['turmas'] = obj_turmas

            obj_professores.append(InsertOne(json_professores))

        collection_professores = scripts_mongodb.db['professores']

        collection_professores.bulk_write(obj_professores)

if __name__ == '__main__':

    config = {
        'number_of_examples': 10,
        'locate': 'pt_BR'
    }

    main(**config)
