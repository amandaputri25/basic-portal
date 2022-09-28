from django.contrib import admin
from django.urls import path
from FKIP.views import index
from FAPERTA.views import situs
from FEB.views import feb
from FH.views import fh
from FISIP.views import fisip
from FK.views import fk
from FT.views import ft
from PASCASARJANA.views import pascasarjana
from PROFIL.views import profil
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', index),
    path('faperta/', situs),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('ft/', ft), 
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    path('', views.index),
]