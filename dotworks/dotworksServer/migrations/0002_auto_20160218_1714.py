# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotworksServer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='e_mail',
        ),
    ]