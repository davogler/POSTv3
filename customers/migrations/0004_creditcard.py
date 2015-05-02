# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0003_auto_20150412_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45, verbose_name=b'Payer first name', blank=True)),
                ('last_name', models.CharField(max_length=45, verbose_name=b'Payer last name', blank=True)),
                ('last4', models.CharField(max_length=120)),
                ('card_type', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Credit Card',
                'verbose_name_plural': 'Credit Cards',
            },
            bases=(models.Model,),
        ),
    ]
