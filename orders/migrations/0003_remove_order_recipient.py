# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150405_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='recipient',
        ),
    ]
