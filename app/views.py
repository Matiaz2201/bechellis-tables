from multiprocessing import context
from django.shortcuts import render
from . models import Clientes, Enderecos, Produtos, Alugueis

# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar_alugueis(request):
    alugueis = Alugueis.objects.filter()
    context = {
        'alugueis' : alugueis
    }
    return render(request, 'lista_alugueis.html', context)

def listar_clientes(request):
    clientes = Enderecos.objects.filter()
    context = {
        'clientes' : clientes
    }
    return render(request, 'listar_clientes.html', context)

def listar_produtos(request):
    produtos = Produtos.objects.filter()
    context = {
        'produtos' : produtos
    }
    return render(request, 'listar_produtos.html', context)