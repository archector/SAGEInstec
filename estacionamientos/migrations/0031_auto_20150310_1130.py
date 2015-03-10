# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0030_auto_20150309_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='Pico_Final',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='Pico_Inicio',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='monto_tarifa_pico',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
            preserve_default=True,
        ),
    ]
