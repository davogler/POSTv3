# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_auto_20150424_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instapost',
            options={'ordering': ['-created_time'], 'verbose_name': 'Instagram Post', 'verbose_name_plural': 'Instagram Posts'},
        ),
        migrations.AddField(
            model_name='igtag',
            name='ig_id',
            field=models.CharField(max_length=200, verbose_name=b'IG ID', blank=True),
            preserve_default=True,
        ),
    ]
