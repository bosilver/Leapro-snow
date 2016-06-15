# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='detail',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='img_profile',
            field=models.ImageField(default=None, null=True, upload_to=b'insturctors'),
            preserve_default=True,
        ),
    ]
