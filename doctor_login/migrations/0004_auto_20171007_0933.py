# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_login', '0003_auto_20171007_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docdetails',
            name='slot1_id',
            field=models.CharField(default='BKID000000000000000', max_length=19),
        ),
    ]
