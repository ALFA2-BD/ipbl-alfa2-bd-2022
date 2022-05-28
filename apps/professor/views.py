from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect

def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('professor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def login_test(request):
    print(request.POST)

    context = {
        'segment': 'login',
        'nome': request.POST['nome_professor'],
        'senha': request.POST['senha_professor']
    }
    html_template = loader.get_template('professor/screens/login_test.html')
    response = redirect('/professor/home')
    return HttpResponse(html_template.render(context, request))

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
    context = {'segment': 'turmas'}
    html_template = loader.get_template('professor/screens/turmas.html')
    return HttpResponse(html_template.render(context, request))
