# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150331_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['-cutoff_date'], 'verbose_name': 'Subscription', 'verbose_name_plural': 'Subscriptions'},
        ),
    ]
