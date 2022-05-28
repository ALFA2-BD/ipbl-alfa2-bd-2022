from django.urls import path, re_path
from apps.gestor import views

urlpatterns = [
    path('login', views.login, name='gestor'),
    path('home', views.home, name='gestor'),
    path('informacoes', views.informacoes, name='gestor'),
    path('escolas', views.escolas, name='gestor'),
    path('gestores_escolares', views.gestores_escolares, name='gestor'),
    path('resumo_coletas', views.resumo_coletas, name='gestor'),
]