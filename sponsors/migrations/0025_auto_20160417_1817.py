# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0024_auto_20160417_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 18, 17, 20, 144592)),
        ),
    ]
