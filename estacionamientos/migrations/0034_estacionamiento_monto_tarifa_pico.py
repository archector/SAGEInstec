# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0033_remove_estacionamiento_monto_tarifa_pico'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='monto_tarifa_pico',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, blank=True, null=True),
            preserve_default=True,
        ),
    ]
