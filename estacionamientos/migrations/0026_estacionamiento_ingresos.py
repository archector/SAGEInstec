# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0025_auto_20150307_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='Ingresos',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
