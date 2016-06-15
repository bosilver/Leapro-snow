# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='ski',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certification',
            name='snowboard',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
