# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-15 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_toverify_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cooperation',
            name='contractee_company',
        ),
        migrations.RemoveField(
            model_name='cooperation',
            name='contractor_company',
        ),
    ]