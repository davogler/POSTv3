# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_creditcard_stripe_id'),
        ('orders', '0006_auto_20150412_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
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
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'Started', max_length=120, choices=[(b'Started', b'Started'), (b'Pending', b'Pending'), (b'Finished', b'Finished'), (b'Recorded', b'Recorded'), (b'Refunded', b'Refunded')]),
            preserve_default=True,
        ),
    ]
