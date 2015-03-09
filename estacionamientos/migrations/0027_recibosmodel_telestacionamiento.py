# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0026_estacionamiento_ingresos'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibosmodel',
            name='TelEstacionamiento',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
