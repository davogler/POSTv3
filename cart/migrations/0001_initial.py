# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('total', models.FloatField(default=0.0)),
                ('item_list', models.CharField(max_length=500, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('line_total', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Subscription', models.ForeignKey(blank=True, to='catalog.Subscription', null=True)),
                ('cart', models.ForeignKey(to='cart.Cart')),
                ('single', models.ForeignKey(blank=True, to='articles.Issue', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
