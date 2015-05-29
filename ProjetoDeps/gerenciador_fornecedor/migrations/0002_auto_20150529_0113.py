# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador_fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='data',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
