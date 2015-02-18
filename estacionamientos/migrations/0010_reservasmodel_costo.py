# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0009_remove_reservasmodel_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservasmodel',
            name='Costo',
            field=models.CharField(null=True, blank=True, max_length=20, default=None),
            preserve_default=True,
        ),
    ]
