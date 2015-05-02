# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instapost',
            name='tag',
            field=models.CharField(max_length=200, verbose_name=b'IG tag', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instapost',
            name='standard_resolution',
            field=models.CharField(max_length=200, verbose_name=b'image URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instapost',
            name='username',
            field=models.CharField(max_length=100, verbose_name=b'IG username', blank=True),
            preserve_default=True,
        ),
    ]
