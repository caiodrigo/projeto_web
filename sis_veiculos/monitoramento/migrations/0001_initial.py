# Generated by Django 5.1.3 on 2024-11-16 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaSaida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('saida', models.DateTimeField(blank=True, null=True)),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoramento.motorista')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoramento.vaga')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoramento.veiculo')),
            ],
        ),
    ]
