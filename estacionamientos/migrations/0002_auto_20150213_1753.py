# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('tipoTarifa', models.CharField(max_length=50, serialize=False, primary_key=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='monto_tarifa',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(default=None, to='estacionamientos.Tarifa'),
            preserve_default=True,
        ),
    ]
