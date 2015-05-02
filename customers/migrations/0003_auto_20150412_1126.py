# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150405_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='first_name',
            field=models.CharField(max_length=45, verbose_name=b'First Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='last_name',
            field=models.CharField(max_length=45, verbose_name=b'Last Name', blank=True),
            preserve_default=True,
        ),
    ]
