# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0004_auto_20150725_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 11, 44, 48, 563576)),
            preserve_default=True,
        ),
    ]
