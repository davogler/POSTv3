# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150331_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 3, 31, 22, 32, 54, 935255), unique=True),
            preserve_default=False,
        ),
    ]
