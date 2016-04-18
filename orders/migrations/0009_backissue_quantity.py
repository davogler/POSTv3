# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_backissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='backissue',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
