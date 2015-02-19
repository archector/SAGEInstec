# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0008_reservasmodel_costo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservasmodel',
            name='Costo',
        ),
    ]
