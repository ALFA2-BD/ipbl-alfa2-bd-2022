from django.urls import path, re_path
from apps.professor import views

urlpatterns = [

    # The home page
    path('login', views.login, name='professor'),
    path('home', views.home, name='professor'),
    path('coleta', views.coleta, name='professor'),
    # path('coleta', views.coleta, name='professor'),
]
