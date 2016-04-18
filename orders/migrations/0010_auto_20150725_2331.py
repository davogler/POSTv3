# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_backissue_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payer_email',
            field=models.EmailField(default='test@test.com', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payer_name',
            field=models.CharField(default='Joe Schmo', max_length=120),
            preserve_default=False,
        ),
    ]
