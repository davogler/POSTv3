# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20150403_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'ABC123', unique=True, max_length=120)),
                ('total', models.FloatField(default=0.0)),
                ('status', models.CharField(default=b'Started', max_length=120, choices=[(b'Started', b'Started'), (b'Pending', b'Pending'), (b'Finished', b'Finished'), (b'Refunded', b'Refunded')])),
                ('requires_shipping', models.BooleanField(default=False)),
                ('notes', models.TextField(null=True, verbose_name=b'Comments', blank=True)),
                ('last4', models.CharField(max_length=120)),
                ('card_type', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(to='cart.Cart')),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(models.Model,),
        ),
    ]
