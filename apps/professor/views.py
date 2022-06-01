from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from dataset.ScriptsMongoDB import ScriptsMongoDB
from utils.DictHelper import DictHelper
from utils.CryptoHelper import CryptoHelper
from bson.objectid import ObjectId
import json
from random import randint

def login(request):
    context = {
        'segment': 'login'
    }
    html_template = loader.get_template('professor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def verify_login(request):

    crypto = CryptoHelper()

    if request.POST:

        scripts_mongodb = ScriptsMongoDB()

        data = request.POST
        identificador_professor = data['identificador_professor']
        senha_professor = data['senha_professor']

        professores = scripts_mongodb.get_data_find(
            collection_name='professores',
            filter = {
                'identificador': identificador_professor
            }
        )

        scripts_mongodb.close_connection()

        if len(professores):

            professor = professores[0]

            if senha_professor == crypto.decrypt_message(professor['hash_senha']):

                context = {
                    'segment': 'home',
                    'err':''
                }

                response = redirect('/professor/home', context)

                response.set_cookie('identificador', professor['identificador'])

                return response

    context = {
        'segment': 'login',
        'err':''
    }

    return redirect('/professor/login', context)

def home(request):
    context = {
        'segment': 'home'
    }

    identificador = request.COOKIES.get('identificador')

    html_template = loader.get_template('professor/screens/home.html')

    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)

    return HttpResponse(html_template.render(context, request))

def coleta(request):

    identificador = request.COOKIES.get('identificador')

    id_aluno  = request.POST['id_aluno']

    scripts_mongodb = ScriptsMongoDB()

    aluno = scripts_mongodb.db['alunos'].find_one(ObjectId(id_aluno))
    professor = scripts_mongodb.db['professores'].find_one({'identificador': identificador})

    frases_tipo_1 = scripts_mongodb.get_data_find(
        collection_name='frases',
        filter = {
            'tipo': 1
        }
    )
    frases_tipo_2 = scripts_mongodb.get_data_find(
        collection_name='frases',
        filter = {
            'tipo': 2
        }
    )
    frases_tipo_3 = scripts_mongodb.get_data_find(
        collection_name='frases',
        filter = {
            'tipo': 3
        }
    )

    frases = {
        'tipo_1': frases_tipo_1[randint(0, len(frases_tipo_1)-1)],
        'tipo_2': frases_tipo_2[randint(0, len(frases_tipo_2)-1)],
        'tipo_3': frases_tipo_3[randint(0, len(frases_tipo_3)-1)],
    }

    scripts_mongodb.close_connection()

    context = {
        'segment': 'coleta',
        'professor': professor,
        'aluno': aluno,
        'frases': frases
    }

    identificador = request.COOKIES.get('identificador')

    html_template = loader.get_template('professor/screens/coleta.html')

    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)

    return response

def submit_audios(request):

    print(request.POST)

    response = HttpResponse(json.dumps(request.POST), content_type="application/json")

    return response

def banco_frases(request):

    scripts_mongodb = ScriptsMongoDB()

    frases = scripts_mongodb.get_collection_data(collection_name='frases')

    scripts_mongodb.close_connection()

    context = {
        'segment': 'banco_frases',
        'frases': frases
    }

    html_template = loader.get_template('professor/screens/banco_frases.html')
    identificador = request.COOKIES.get('identificador')

    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)
    return response

def informacoes(request):

    identificador = request.COOKIES.get('identificador')

    scripts_mongodb = ScriptsMongoDB()

    professor = scripts_mongodb.get_data_find(
        collection_name='professores',
        filter = {'identificador': identificador}
    )[0]

    scripts_mongodb.close_connection()

    context = {
        'segment': 'informacoes',
        'professor': professor,
    }

    html_template = loader.get_template('professor/screens/informacoes.html')

    response = HttpResponse(html_template.render(context, request))

    response.set_cookie('identificador', identificador)

    return response

def turmas(request):

    identificador = request.COOKIES.get('identificador')

    scripts_mongodb = ScriptsMongoDB()

    professor = scripts_mongodb.get_data_find(
        collection_name='professores',
        filter = {
            'identificador': identificador
        }
    )[0]

    turmas = scripts_mongodb.get_data_find(
        collection_name='turmas',
        filter = {
            "professor": professor
        }
    )

    scripts_mongodb.close_connection()

    for i in range(len(turmas)):
        turmas[i]['quant_alu'] = len(turmas[i]['alunos'])
        turmas[i]['id_turma'] = str(turmas[i].get('_id'))

    context = {
        'segment': 'turmas',
        'turmas': turmas,
    }

    html_template = loader.get_template('professor/screens/turmas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)
    return response

def alunos(request):

    identificador = request.COOKIES.get('identificador')

    if request.POST:

        id_turma = request.POST['id_turma']

        scripts_mongodb = ScriptsMongoDB()

        turma = scripts_mongodb.db['turmas'].find_one(ObjectId(id_turma))

        scripts_mongodb.close_connection()

        alunos = turma['alunos']

        for i in range(len(alunos)):
            alunos[i]['id_aluno'] = str(alunos[i].get('_id'))

        context = {
            'segment': 'alunos',
            'alunos': alunos
        }

        html_template = loader.get_template('professor/screens/alunos.html')
        response = HttpResponse(html_template.render(context, request))
        response.set_cookie('identificador', identificador)
        return response

    context = {
        'segment': 'home',
    }
    response = redirect('/professor/home', context)
    response.set_cookie('identificador', identificador)
    return response
