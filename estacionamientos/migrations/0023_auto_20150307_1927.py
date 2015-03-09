# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0022_auto_20150305_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibosmodel',
            name='NomnbreEstacionamiento',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibosmodel',
            name='RifEstacionamiento',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
