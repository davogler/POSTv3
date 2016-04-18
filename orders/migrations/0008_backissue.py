# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_creditcard_stripe_id'),
        ('orders', '0007_auto_20150723_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackIssue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('originating_order', models.ForeignKey(blank=True, to='orders.Order', null=True)),
                ('recipient', models.ForeignKey(blank=True, to='customers.Recipient', null=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Back Issue',
                'verbose_name_plural': 'Back Issues',
            },
            bases=(models.Model,),
        ),
    ]
