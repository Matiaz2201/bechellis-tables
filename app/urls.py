from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('home/', views.home),
    path('alugueis/listar', views.listar_alugueis, name='listar_aluguel'),
    path('clientes/listar', views.listar_clientes, name='listar_clientes'),
    path('produtos/listar', views.listar_produtos, name='listar_produtos')

]
