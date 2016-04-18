# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20150405_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='term',
            field=models.IntegerField(default=6),
            preserve_default=True,
        ),
    ]
