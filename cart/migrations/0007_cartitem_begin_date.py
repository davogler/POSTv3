# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cartitem_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='begin_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
