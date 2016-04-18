# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_subscription_first_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='type',
            field=models.IntegerField(default=3, choices=[(1, b'Rolling One Year'), (2, b'Renewal'), (3, b'Other')]),
        ),
    ]
