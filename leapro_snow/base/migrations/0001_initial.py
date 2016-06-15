# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('img', models.ImageField(upload_to=b'carousel')),
                ('text', models.TextField(default=None, null=True, blank=True)),
                ('slide_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=50)),
                ('img_head', models.ImageField(default=None, upload_to=b'insturctors')),
                ('ski', models.BooleanField(default=None)),
                ('snowboard', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
