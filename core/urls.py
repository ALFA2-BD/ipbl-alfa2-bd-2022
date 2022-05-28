from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include("apps.authentication.urls")),
    # path("", include("apps.home.urls"),
    path("professor/", include("apps.professor.urls")),
    path("gestor/", include("apps.gestor.urls"))
]
