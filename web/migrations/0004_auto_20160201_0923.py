# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160201_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationlinks',
            old_name='categroy',
            new_name='category',
        ),
    ]
