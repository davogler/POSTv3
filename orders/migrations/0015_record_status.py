# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20170125_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.CharField(blank=True, max_length=120, null=True, choices=[(b'Notified', b'Notified'), (b'Renewed', b'Renewed'), (b'Borked', b'Borked'), (b'Refunded', b'Refunded')]),
        ),
    ]
