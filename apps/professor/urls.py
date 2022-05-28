from django.urls import path, re_path
from psutil import virtual_memory
from apps.professor import views

urlpatterns = [

    # The home page
    path('login', views.login, name='professor'),
    path('login_test', views.login_test, name='professor'),
    path('home', views.home, name='professor'),
    path('coleta', views.coleta, name='professor'),
    path('informacoes', views.informacoes, name='professor'),
    path('turmas', views.turmas, name='professor'),
    path('banco_frases', views.banco_frases, name='professor'),
    # path('coleta', views.coleta, name='professor'),
]
