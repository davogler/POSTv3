# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0016_auto_20160125_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 22, 20, 33, 261556)),
            preserve_default=True,
        ),
    ]
