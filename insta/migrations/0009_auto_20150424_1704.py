# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_auto_20150424_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instapost',
            name='profile_picture',
            field=models.URLField(max_length=500, verbose_name=b'Profile Pic URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instapost',
            name='tag',
            field=models.ForeignKey(blank=True, to='insta.IGTag', null=True),
            preserve_default=True,
        ),
    ]
