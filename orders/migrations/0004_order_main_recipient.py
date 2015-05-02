# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150412_1126'),
        ('orders', '0003_remove_order_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='main_recipient',
            field=models.ForeignKey(blank=True, to='customers.Recipient', null=True),
            preserve_default=True,
        ),
    ]
