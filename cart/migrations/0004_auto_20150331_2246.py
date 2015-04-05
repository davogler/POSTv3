# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='slug',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='flug',
            field=models.SlugField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
