# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0019_recibosmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibosmodel',
            name='NumeroTransaccion',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
