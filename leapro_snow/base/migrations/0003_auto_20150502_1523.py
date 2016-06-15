# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150502_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='img_profile',
        ),
    ]
