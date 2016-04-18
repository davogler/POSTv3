# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160407_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 15, 32, 8, 270806)),
        ),
    ]
