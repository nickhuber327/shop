# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='static/shop/img/'),
        ),
    ]
