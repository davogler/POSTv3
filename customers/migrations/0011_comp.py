# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_auto_20170124_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('recipient_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='customers.Recipient')),
                ('comp_type', models.CharField(default=b'VIP', max_length=120, choices=[(b'Promo', b'Promo'), (b'Staff', b'Staff'), (b'Advertiser', b'Advertiser'), (b'VIP', b'VIP'), (b'Winner', b'Winner')])),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['last_name'],
                'verbose_name_plural': 'Comp Recipients',
            },
            bases=('customers.recipient',),
        ),
    ]
