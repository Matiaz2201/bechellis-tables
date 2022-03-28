import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()

class Enderecos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    valor_patrimonio = models.DecimalField(decimal_places=2,max_digits=14)

class Alugueis(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    data_aluguel = models.DateField()
    data_entrega = models.DateField()
    entregue = models.BooleanField()
    description = models.CharField(max_length=255)