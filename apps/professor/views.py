from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
from dataset.ScriptsMongoDB import ScriptsMongoDB
import json

def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('professor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def verify_login(request):

    if request.POST:

        scripts_mongodb = ScriptsMongoDB()

        data = request.POST
        identificador_professor = data['identificador_professor']
        senha_professor = data['senha_professor']

        professor = scripts_mongodb.get_data_find(
            collection_name='professores',
            filter = {'cpf': '123.870.496-40'}
        )[0]

        scripts_mongodb.close_connection()

        if senha_professor == professor['senha']:

            context = {
                'segment': 'home',
                'err':''
            }
            return redirect('/professor/home', context)

    context = {
        'segment': 'login',
        'err':''
    }

    return redirect('/professor/login', context)

def home(request):
    context = {'segment': 'home'}
    html_template = loader.get_template('professor/screens/home.html')
    return HttpResponse(html_template.render(context, request))

def coleta(request):
    context = {'segment': 'coleta'}
    html_template = loader.get_template('professor/screens/coleta.html')
    return HttpResponse(html_template.render(context, request))

def banco_frases(request):
    context = {'segment': 'banco_frases'}
    html_template = loader.get_template('professor/screens/banco_frases.html')
    return HttpResponse(html_template.render(context, request))

def informacoes(request):
    context = {'segment': 'informacoes'}
    html_template = loader.get_template('professor/screens/informacoes.html')
    return HttpResponse(html_template.render(context, request))

def turmas(request):

    scripts_mongodb = ScriptsMongoDB()

    professor = scripts_mongodb.get_data_find(
        collection_name='professores',
        filter = {'cpf': '123.870.496-40'}
    )[0]

    turmas = [] if 'turmas' not in professor else professor['turmas']

    scripts_mongodb.close_connection()

    for i in range(len(turmas)):
        turmas[i]['quant_alu'] = len(turmas[i]['alunos'])

    context = {
        'segment': 'turmas',
        'turmas': turmas,
    }

    html_template = loader.get_template('professor/screens/turmas.html')
    return HttpResponse(html_template.render(context, request))

def alunos(request):

    if request.POST:

        alunos = request.POST['alunos']

        context = {
            'segment': 'alunos',
            'alunos': json.loads(alunos.replace("\'", '\"'))
        }
        html_template = loader.get_template('professor/screens/alunos.html')
        return HttpResponse(html_template.render(context, request))

    context = {
        'segment': 'home',
    }
    return redirect('/professor/home', context)
