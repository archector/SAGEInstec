# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0015_auto_20150219_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservasmodel',
            name='Costo',
        ),
    ]
