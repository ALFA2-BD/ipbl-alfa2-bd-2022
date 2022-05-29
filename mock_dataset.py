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

    ### Fake Phrases ###

    obj_frases = []
    for _ in range(number_of_examples):
        json_frase = {
            'frase': fake.catch_phrase(),
            'tipo': randint(1, 3)
        }
        obj_frases.append(InsertOne(json_frase))

    collection_frases = scripts_mongodb.db['frases']

    collection_frases.bulk_write(obj_frases)


if __name__ == '__main__':

    config = {
        'number_of_examples': 10,
        'locate': 'pt_BR'
    }

    main(**config)
