# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rua', models.CharField(max_length=21)),
                ('pais', models.CharField(max_length=21)),
                ('cidade', models.CharField(max_length=21)),
                ('estado', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=31)),
                ('telefone', models.CharField(max_length=15)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='endereco',
            name='fornecedor',
            field=models.ForeignKey(to='gerenciador_fornecedor.Fornecedor'),
        ),
    ]
