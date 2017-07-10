# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170614_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=30, blank=True)),
                ('user_password', models.CharField(max_length=30, blank=True)),
                ('user_emial', models.CharField(max_length=30, blank=True)),
            ],
        ),
    ]
