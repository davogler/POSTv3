# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line1', models.CharField(max_length=45, verbose_name=b'Address line 1')),
                ('address_line2', models.CharField(max_length=45, verbose_name=b'Address line 2', blank=True)),
                ('postal_code', models.CharField(max_length=10, verbose_name=b'Postal Code')),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=40, verbose_name=b'State/Province', blank=True)),
                ('country', models.CharField(max_length=40, verbose_name=b'Country', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45, verbose_name=b'Address line 1', blank=True)),
                ('last_name', models.CharField(max_length=45, verbose_name=b'Address line 1', blank=True)),
                ('org', models.CharField(max_length=45, verbose_name=b'Organization/Business', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Recipients',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='recipient',
            field=models.ForeignKey(to='customers.Recipient'),
            preserve_default=True,
        ),
    ]
