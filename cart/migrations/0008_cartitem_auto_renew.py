# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem_begin_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='auto_renew',
            field=models.BooleanField(default=True),
        ),
    ]
