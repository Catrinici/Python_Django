# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserManager',
        ),
    ]
