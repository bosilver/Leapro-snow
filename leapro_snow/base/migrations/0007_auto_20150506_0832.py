# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150506_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='cert',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='img_profile',
            field=models.ImageField(default=None, null=True, upload_to=b'insturctors', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='location',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='mostlike_ski_field',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='ski_field',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='vedio',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='want_to_say',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
