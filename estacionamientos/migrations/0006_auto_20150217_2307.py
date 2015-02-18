# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0005_reservasmodel_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasmodel',
            name='Costo',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
