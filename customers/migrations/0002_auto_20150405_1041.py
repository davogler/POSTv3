# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='recipient',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='recipient',
            name='address_line1',
            field=models.CharField(max_length=45, verbose_name=b'Address line 1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='address_line2',
            field=models.CharField(max_length=45, verbose_name=b'Address line 2', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='city',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='country',
            field=models.CharField(max_length=40, verbose_name=b'Country', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name=b'Postal Code', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='state_province',
            field=models.CharField(max_length=40, verbose_name=b'State/Province', blank=True),
            preserve_default=True,
        ),
    ]
