# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0011_auto_20150425_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100, null=True, verbose_name=b'IG username', blank=True)),
                ('user_id', models.CharField(max_length=100, null=True, verbose_name=b'IG user ID', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Bad Instagrammer',
                'verbose_name_plural': 'Bad People',
            },
            bases=(models.Model,),
        ),
    ]
