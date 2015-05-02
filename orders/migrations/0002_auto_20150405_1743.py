# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150405_1041'),
        ('orders', '0001_initial'),
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
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Credit Card',
                'verbose_name_plural': 'Credit Cards',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='order',
            name='card_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last4',
        ),
        migrations.RemoveField(
            model_name='order',
            name='requires_shipping',
        ),
        migrations.AddField(
            model_name='order',
            name='credit_card',
            field=models.ForeignKey(blank=True, to='orders.CreditCard', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='recipient',
            field=models.ManyToManyField(to='customers.Recipient'),
            preserve_default=True,
        ),
    ]
