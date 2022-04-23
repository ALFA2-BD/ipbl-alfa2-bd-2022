from django.urls import path

from . import views

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.login, name='login'),
    # path('admin/', admin.site.urls),
]