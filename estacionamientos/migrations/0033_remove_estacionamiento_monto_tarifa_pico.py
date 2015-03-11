# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0032_auto_20150310_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamiento',
            name='monto_tarifa_pico',
        ),
    ]
