# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150405_1041'),
        ('cart', '0005_auto_20150403_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='recipient',
            field=models.ForeignKey(blank=True, to='customers.Recipient', null=True),
            preserve_default=True,
        ),
    ]
