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
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('sku', models.CharField(help_text=b'Enter as ABC-##', max_length=200)),
                ('cutoff_date', models.DateTimeField(default=datetime.datetime.now, help_text=b'Last date to order subscription and still get this issue', blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.FloatField(default=0.0, help_text=b'Not used right now')),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'Item Image, 600-800px wide', max_length=200, null=True, verbose_name=b'Item Image', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('title', 'slug')]),
        ),
    ]
