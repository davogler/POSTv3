# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0008_auto_20150725_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 17, 6, 51, 274906)),
            preserve_default=True,
        ),
    ]
