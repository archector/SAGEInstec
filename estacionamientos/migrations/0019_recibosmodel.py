# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0018_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecibosModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cedula', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('NumeroTarjeta', models.CharField(default=None, max_length=16, null=True, blank=True)),
                ('FechaPago', models.DateTimeField(default=None)),
                ('InicioReserva', models.DateTimeField(default=None)),
                ('FinalReserva', models.DateTimeField(default=None)),
                ('Costo', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('NumeroTransaccion', models.ForeignKey(to='estacionamientos.ReservasModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
