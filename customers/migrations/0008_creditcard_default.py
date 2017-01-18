# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20160410_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]
