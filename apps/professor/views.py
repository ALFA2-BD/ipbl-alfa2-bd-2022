from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('professor/screens/login.html')
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

# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
