# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_order_main_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='credit_card',
        ),
        migrations.DeleteModel(
            name='CreditCard',
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
