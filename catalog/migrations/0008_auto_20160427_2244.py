# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20160408_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['-first_issue'], 'verbose_name': 'Subscription', 'verbose_name_plural': 'Subscriptions'},
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='cutoff_date',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.FloatField(default=7.0, help_text=b'Cover Price'),
        ),
    ]
