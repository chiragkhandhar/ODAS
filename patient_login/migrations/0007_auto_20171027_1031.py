# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_login', '0006_remove_userprofile_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[(b'male', b'Male'), (b'female', b'Female')], max_length=6),
        ),
    ]
