# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0012_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasmodel',
            name='FinalReserva',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservasmodel',
            name='InicioReserva',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
