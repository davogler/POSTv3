# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20160408_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 10, 22, 58, 6, 502608)),
        ),
    ]
