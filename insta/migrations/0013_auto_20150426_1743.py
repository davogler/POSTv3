# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0012_badperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igtag',
            name='ig_id',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'IG ID', blank=True),
            preserve_default=True,
        ),
    ]
