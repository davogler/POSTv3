# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0029_auto_20160427_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
