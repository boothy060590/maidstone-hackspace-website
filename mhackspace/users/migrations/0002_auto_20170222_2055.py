# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Guest user'), (1, 'Active membership'), (3, 'Membership Expired'), (4, 'Membership Cancelled')], default=0),
        ),
    ]
