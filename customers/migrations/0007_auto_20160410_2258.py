# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_recipient_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='payer_email',
            field=models.CharField(max_length=200, verbose_name=b'Payer full name', blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='payer_name',
            field=models.CharField(max_length=250, verbose_name=b'Payer full name', blank=True),
        ),
    ]
