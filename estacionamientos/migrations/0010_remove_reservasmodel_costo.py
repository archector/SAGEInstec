# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0009_auto_20150219_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservasmodel',
            name='Costo',
        ),
    ]
