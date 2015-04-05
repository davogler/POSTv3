# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20150331_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_total',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='shipping_total',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='shipping_line_total',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
