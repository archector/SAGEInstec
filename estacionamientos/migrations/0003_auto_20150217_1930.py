# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20150213_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(default=None, blank=True, to='estacionamientos.Tarifa', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='monto_tarifa',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
