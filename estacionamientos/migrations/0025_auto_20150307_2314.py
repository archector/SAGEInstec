# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0024_auto_20150307_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibosmodel',
            name='Costo',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
