# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_igtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instapost',
            name='tag',
            field=models.ForeignKey(to='insta.IGTag'),
            preserve_default=True,
        ),
    ]
