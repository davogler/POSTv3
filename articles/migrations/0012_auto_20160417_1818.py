# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20160417_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 18, 18, 54, 911362)),
        ),
    ]
