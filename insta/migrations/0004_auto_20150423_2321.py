# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20150423_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instapost',
            name='created_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
