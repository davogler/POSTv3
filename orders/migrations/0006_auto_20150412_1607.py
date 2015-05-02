# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20150412_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='owner',
            new_name='user',
        ),
    ]
