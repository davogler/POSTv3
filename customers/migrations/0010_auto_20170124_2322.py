# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_recipient_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipient',
            options={'ordering': ['last_name'], 'verbose_name_plural': 'Recipients'},
        ),
    ]
