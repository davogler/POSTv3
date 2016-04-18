# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20160407_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.FloatField(default=0.0),
        ),
    ]
