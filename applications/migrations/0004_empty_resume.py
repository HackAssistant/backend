# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-17 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
    ]
