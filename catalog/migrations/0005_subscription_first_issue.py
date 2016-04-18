# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_subscription_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='first_issue',
            field=models.IntegerField(default=12, help_text=b'Integer value of first issue'),
            preserve_default=False,
        ),
    ]
