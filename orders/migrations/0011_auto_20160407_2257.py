# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20150725_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payer_email',
            field=models.EmailField(max_length=254),
        ),
    ]
