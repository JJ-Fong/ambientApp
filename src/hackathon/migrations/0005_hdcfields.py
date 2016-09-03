# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-03 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_auto_20160901_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDCFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.IntegerField()),
                ('personasxcasa', models.IntegerField()),
                ('tiempoxbano', models.IntegerField()),
                ('apagarluz', models.IntegerField()),
                ('vehiculosxcasa', models.IntegerField()),
                ('transporte', models.IntegerField()),
                ('frutasyverduras', models.IntegerField()),
                ('comidarapida', models.IntegerField()),
                ('comidaenlatada', models.IntegerField()),
                ('bolsasplasticas', models.IntegerField()),
                ('hojas2uso', models.IntegerField()),
            ],
        ),
    ]
