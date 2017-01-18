# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20160427_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.FloatField(default=36.0, help_text=b'Cover Price'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='term',
            field=models.IntegerField(default=4, help_text=b'default 4 issues in one year'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='title',
            field=models.CharField(default=b'One-Year Subscription', max_length=200),
        ),
    ]
