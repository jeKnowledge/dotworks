# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 21:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dotworks_server', '0005_auto_20160322_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='area',
            field=models.CharField(default='Informatica', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='beggining_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 3, 29, 21, 54, 22, 600279, tzinfo=utc), verbose_name='Beggining date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 mês'), (2, '2 meses'), (3, '3 meses'), (4, '4 meses'), (5, '5 meses'), (6, '6 meses'), (7, '7 meses'), (8, '8 meses'), (9, '9 meses'), (10, '10 meses'), (11, '11 meses'), (12, '12 meses')], default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='location',
            field=models.CharField(default='Lisbon', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='n_positions',
            field=models.SmallIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='payment',
            field=models.CharField(default='Não Remunerado', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='working_time',
            field=models.CharField(choices=[('P_T', 'Part time'), ('F_T', 'Full time')], default='Pat_Time', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internship',
            name='application_deadline',
            field=models.DateField(verbose_name='aplications deadline'),
        ),
    ]