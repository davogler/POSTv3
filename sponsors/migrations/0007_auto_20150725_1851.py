# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0006_auto_20150725_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 18, 51, 47, 658115)),
            preserve_default=True,
        ),
    ]
