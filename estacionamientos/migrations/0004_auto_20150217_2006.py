# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0003_auto_20150217_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='monto_tarifa',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
