from django.urls import path, re_path
from psutil import virtual_memory
from apps.professor import views

urlpatterns = [

    # The home page
    path('login', views.login, name='professor'),
    path('verify_login', views.verify_login, name='professor'),

    path('home', views.home, name='professor'),
    path('informacoes', views.informacoes, name='professor'),

    path('turmas', views.turmas, name='professor'),
    path('alunos', views.alunos, name='professor'),

    path('coleta', views.coleta, name='professor'),
    path('submit_audios', views.submit_audios, name='professor'),

    path('banco_frases', views.banco_frases, name='professor'),
    path('view_audio_metrics', views.view_audio_metrics, name='professor'),
]
