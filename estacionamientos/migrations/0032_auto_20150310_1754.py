# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0031_auto_20150310_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='monto_tarifa_pico',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, default=0, blank=True),
            preserve_default=True,
        ),
    ]
