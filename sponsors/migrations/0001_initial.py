# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('adimg', filebrowser.fields.FileBrowseField(help_text=b'Upload an image to be used for advertising: 768x90', max_length=200, null=True, verbose_name=b'Ad Image', blank=True)),
                ('adlink', models.URLField()),
                ('position', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2015, 5, 31, 15, 2, 41, 125145))),
            ],
            options={
                'ordering': ['-add_date'],
                'verbose_name_plural': 'Advertisement Banners',
            },
            bases=(models.Model,),
        ),
    ]
