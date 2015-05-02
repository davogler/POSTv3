# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_auto_20150424_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instapost',
            options={'ordering': ['timestamp'], 'verbose_name': 'Instagram Post', 'verbose_name_plural': 'Instagram Posts'},
        ),
        migrations.AddField(
            model_name='instapost',
            name='profile_picture',
            field=models.URLField(max_length=500, verbose_name=b'Link to IG post', blank=True),
            preserve_default=True,
        ),
    ]
