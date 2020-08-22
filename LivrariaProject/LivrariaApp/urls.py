from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^livro_list/', livro_list, name='listar_livros'),
]