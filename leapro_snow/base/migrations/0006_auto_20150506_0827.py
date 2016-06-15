# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20150505_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='profile_url',
        ),
        migrations.AddField(
            model_name='instructor',
            name='cert',
            field=models.TextField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='img_profile',
            field=models.ImageField(default=None, null=True, upload_to=b'insturctors'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='location',
            field=models.CharField(default=None, max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='mostlike_ski_field',
            field=models.CharField(default=None, max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='page_name',
            field=models.CharField(default=None, max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='ski_field',
            field=models.TextField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='vedio',
            field=models.TextField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='want_to_say',
            field=models.TextField(default=None, null=True),
            preserve_default=True,
        ),
    ]
