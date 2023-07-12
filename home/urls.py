from django.urls import path
from . import views
from home.views import contato

urlpatterns = [
    path("", views.index, name="index"),
    path("/sobre", views.sobre, name="sobre"),
    path("/galeria", views.galeria, name="galeria"),
    path("/marcas", views.marcas, name="marcas"),
    path("/artes", views.artes, name="artes"),
    path("/monstros", views.monstros, name="monstros"),
    path("/contato", views.contato, name="contato")
]