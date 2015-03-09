# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0023_auto_20150307_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recibosmodel',
            old_name='NomnbreEstacionamiento',
            new_name='NombreEstacionamiento',
        ),
    ]
