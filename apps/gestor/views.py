from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('gestor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def home(request):
    context = {'segment': 'home'}
    html_template = loader.get_template('gestor/screens/home.html')
    return HttpResponse(html_template.render(context, request))

def informacoes(request):
    context = {'segment': 'informacoes'}
    html_template = loader.get_template('gestor/screens/informacoes.html')
    return HttpResponse(html_template.render(context, request))

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