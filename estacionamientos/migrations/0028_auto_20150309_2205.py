# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0027_recibosmodel_telestacionamiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='monto_tarifa',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reservasmodel',
            name='Costo',
            field=models.DecimalField(default=None, null=True, max_digits=20, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
