# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstaPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('insta_id', models.CharField(max_length=200, verbose_name=b'IG id', blank=True)),
                ('username', models.CharField(max_length=45, verbose_name=b'IG username', blank=True)),
                ('link', models.URLField(max_length=100, verbose_name=b'Link to IG post', blank=True)),
                ('thumbnail', models.CharField(max_length=200, verbose_name=b'thumbnail URL', blank=True)),
                ('standard_resolution', models.CharField(max_length=45, verbose_name=b'image URL', blank=True)),
                ('caption_text', models.TextField(verbose_name=b'Caption', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Instagram Post',
                'verbose_name_plural': 'Instagram Posts',
            },
            bases=(models.Model,),
        ),
    ]
