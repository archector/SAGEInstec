# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0010_remove_reservasmodel_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservasmodel',
            name='Costo',
            field=models.CharField(default=None, null=True, max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
