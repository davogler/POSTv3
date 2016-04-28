# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20160427_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='image',
            field=filebrowser.fields.FileBrowseField(help_text=b'Item Image', max_length=200, null=True, verbose_name=b'Item Image', blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='sku',
            field=models.CharField(help_text=b'Enter as pb[year][first month][second month]', max_length=200),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='term',
            field=models.IntegerField(default=6, help_text=b'default 6 issues in one year'),
        ),
    ]
