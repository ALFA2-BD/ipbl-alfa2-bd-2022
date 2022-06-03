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

    identificador = request.COOKIES.get('identificador')

    scripts_mongodb = ScriptsMongoDB()

    escolas = scripts_mongodb.get_data_find(
        collection_name='gestores',
        filter = {'identificador': identificador}
    )[0]['escolas']

    scripts_mongodb.close_connection()
    escolas_federais = []
    escolas_estaduais = []
    escolas_municipais = []
    for escola in escolas:
        if(escola["depen_admin"] == 1):
            escolas_federais.append(escola)
        elif(escola["depen_admin"] == 2):
            escolas_estaduais.append(escola)
        elif(escola["depen_admin"] == 3):
            escolas_municipais.append(escola)
    context = {
        'segment': 'escolas',
        'escolas_federais': escolas_federais,
        'escolas_estaduais': escolas_estaduais,
        'escolas_municipais': escolas_municipais,
        'escolas': escolas,
    }
    html_template = loader.get_template('gestor/screens/escolas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)

    return response

def gestores_escolares(request):
    identificador = request.COOKIES.get('identificador')

    scripts_mongodb = ScriptsMongoDB()

    escolas_query = scripts_mongodb.get_data_find(
        collection_name='gestores',
        filter = {'identificador': identificador}
    )[0]['escolas']
    scripts_mongodb.close_connection()

    escolas = []
    labels_chart = []
    data_chart = []
    total_turmas = 0

    for escola in escolas_query:
        labels_chart.append(escola["nome"])
        data_chart.append(len(escola["turmas"]))
        escolas.append({
            "nome": escola["nome"],
            "quantidade": len(escola["turmas"])
        })
        total_turmas += len(escola["turmas"])

    context = {
        'segment': 'gestores_escolares',
        'escolas': escolas,
        'total_turmas': total_turmas,
        'labels_chart': labels_chart[:5],
        'data_chart': data_chart[:5]
    }

    html_template = loader.get_template('gestor/screens/gestores_escolares.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)

    return response


def resumo_coletas(request):
    identificador = request.COOKIES.get('identificador')

    scripts_mongodb = ScriptsMongoDB()

    escolas_query = scripts_mongodb.get_data_find(
        collection_name='gestores',
        filter = {'identificador': identificador}
    )[0]['escolas']
    scripts_mongodb.close_connection()

    list_alunos = []
    escolas = []

    for escola in escolas_query:
        escola_aux = {"nome": escola["nome"], "alunos": []}
        for turma in escola["turmas"]:
            escola_aux['alunos'] = escola_aux['alunos'] + turma["alunos"]
            list_alunos = list_alunos + turma["alunos"]
        escolas.append(escola_aux)

    avaliacoes = {}

    for aluno in list_alunos:
        avaliacoes[aluno] = scripts_mongodb.get_data_find(
                collection_name='alunos',
                filter = {'_id': aluno}
            )[0]["avaliacao"]

    list_avaliacoes = {}
    for key in avaliacoes:
        list_avaliacoes[avaliacoes[key]] = scripts_mongodb.get_data_find(
                collection_name='avaliacoes',
                filter = {'_id': avaliacoes[key]}
            )[0]
    scripts_mongodb.close_connection()

    escolas_name_label = []
    mean_av1 = []
    mean_av2 = []
    mean_av3 = []

    for escola in escolas:
        escolas_name_label.append(escola["nome"])
        av1 = 0
        cont1 = 0
        av2 = 0
        cont2 = 0
        av3 = 0
        cont3 = 0
        for aluno in escola["alunos"]:
            avaliacao_id = avaliacoes[aluno]
            avaliacao = list_avaliacoes[avaliacao_id]["avaliacoes"]
            for coleta in avaliacao[0]["coleta"]:
                if(coleta["metrica"] != None):
                    av1 += coleta["metrica"]
                    cont1 += 1
            for coleta in avaliacao[1]["coleta"]:
                if(coleta["metrica"] != None):
                    av2 += coleta["metrica"]
                    cont2 += 1
            for coleta in avaliacao[2]["coleta"]:
                if(coleta["metrica"] != None):
                    av3 += coleta["metrica"]
                    cont3 += 1
        mean_av1.append(av1/cont1)
        mean_av2.append(av2/cont2)
        mean_av3.append(av3/cont3)

    context = {
        'segment': 'resumo_coletas',
        'avaliacoes': list_avaliacoes,
        "escolas_name_label":   escolas_name_label,
        "mean_av1": mean_av1,
        "mean_av2": mean_av2,
        "mean_av3": mean_av3
    }
    html_template = loader.get_template('gestor/screens/resumo_coletas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador', identificador)

    return response