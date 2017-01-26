# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20170124_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='has_coupon',
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, to='orders.Coupon', null=True),
        ),
    ]
