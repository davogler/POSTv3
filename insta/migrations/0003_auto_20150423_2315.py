# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20150422_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='instapost',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instapost',
            name='created_time',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
