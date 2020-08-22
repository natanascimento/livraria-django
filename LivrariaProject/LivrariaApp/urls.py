from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^livro_list/', livro_list, name='listar_livros'),
    url(r'^livro_new/', livro_new, name='livro_new'),
    url(r'^livro_edit/(?P<pk>[0-9]+)', livro_edit, name='livro_edit'),
]