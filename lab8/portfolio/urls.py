from django.shortcuts import render
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_page_view, name='home')
    path('apresentacao', views.apresentacao_page_view, name='apresentacao')
    path('competencias', views.competencias_page_view, name='competencias')
    path('formacao', views.formacao_page_view, name='formacao')
    path('projetos', views.projetos_page_view, name='projetos')
]