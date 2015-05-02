# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_creditcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='stripe_id',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
