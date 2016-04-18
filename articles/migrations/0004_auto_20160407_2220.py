# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160407_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 22, 20, 47, 407434)),
            preserve_default=True,
        ),
    ]
