# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_shipping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percent_discount', models.DecimalField(default=0.0, max_digits=4, decimal_places=1)),
                ('code', models.CharField(default=b'ABC123', unique=True, max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='has_coupon',
            field=models.NullBooleanField(default=False),
        ),
    ]
