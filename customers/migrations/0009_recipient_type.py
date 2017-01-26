# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_creditcard_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='type',
            field=models.CharField(default=b'Standard', max_length=120, choices=[(b'Standard', b'Standard'), (b'Promo', b'Promo'), (b'Staff', b'Staff')]),
        ),
    ]
