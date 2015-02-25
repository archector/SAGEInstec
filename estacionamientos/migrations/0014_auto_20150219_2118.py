# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0013_auto_20150219_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasmodel',
            name='FinalReserva',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservasmodel',
            name='InicioReserva',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
