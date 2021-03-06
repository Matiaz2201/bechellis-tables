# Generated by Django 4.0.3 on 2022-03-23 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('valor_patrimonio', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Alugueis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_aluguel', models.DateField()),
                ('data_entrega', models.DateField()),
                ('entregue', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produtos')),
            ],
        ),
    ]
