# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '__first__'),
        ('insta', '0005_auto_20150423_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='IGTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=200, verbose_name=b'IG tag', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('articles', models.ManyToManyField(to='articles.Article', null=True, blank=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Instagram Tag',
                'verbose_name_plural': 'Instagram Tags',
            },
            bases=(models.Model,),
        ),
    ]
