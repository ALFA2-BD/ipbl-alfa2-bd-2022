from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from dataset.ScriptsMongoDB import ScriptsMongoDB
from utils.DictHelper import DictHelper
from utils.CryptoHelper import CryptoHelper
from bson.objectid import ObjectId
import json
from random import randint


def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('gestor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def verify_login(request):

    crypto = CryptoHelper()

    if request.POST:

        scripts_mongodb = ScriptsMongoDB()

        data = request.POST
        identificador_professor = data['identificador_gestor']
        senha_gestor = data['senha_gestor']

        gestores = scripts_mongodb.get_data_find(
            collection_name='gestores',
            filter = {
                'identificador': identificador_professor
            }
        )

        scripts_mongodb.close_connection()

        if len(gestores):

            gestor = gestores[0]

            if senha_gestor == crypto.decrypt_message(gestor['hash_senha']):

                context = {
                    'segment': 'home',
                    'err':''
                }

                response = redirect('/gestor/home', context)

                response.set_cookie('identificador', gestor['identificador'])

                return response

    context = {
        'segment': 'login',
        'err':''
    }

    return redirect('/gestor/login', context)

def home(request):
    context = {'segment': 'home'}
    html_template = loader.get_template('gestor/screens/home.html')
    return HttpResponse(html_template.render(context, request))

def informacoes(request):

    identificador = request.COOKIES.get('identificador')

    scripts_mongodb = ScriptsMongoDB()

    gestor = scripts_mongodb.get_data_find(
        collection_name='gestores',
        filter = {'identificador': identificador}
    )[0]

    scripts_mongodb.close_connection()

    context = {
        'segment': 'informacoes',
        'gestor': gestor,
    }

    html_template = loader.get_template('gestor/screens/informacoes.html')

    response = HttpResponse(html_template.render(context, request))

    response.set_cookie('identificador', identificador)

    return response

def escolas(request):
    context = {'segment': 'escolas'}
    html_template = loader.get_template('gestor/screens/escolas.html')
    return HttpResponse(html_template.render(context, request))

def gestores_escolares(request):
    context = {'segment': 'gestores_escolares'}
    html_template = loader.get_template('gestor/screens/gestores_escolares.html')
    return HttpResponse(html_template.render(context, request))

def resumo_coletas(request):
    context = {'segment': 'resumo_coletas'}
    html_template = loader.get_template('gestor/screens/resumo_coletas.html')
    return HttpResponse(html_template.render(context, request))