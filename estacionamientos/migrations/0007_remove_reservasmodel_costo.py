# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0006_auto_20150217_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservasmodel',
            name='Costo',
        ),
    ]
