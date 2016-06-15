# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150502_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='profile_url',
            field=models.URLField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
