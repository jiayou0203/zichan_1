# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_blog_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog_user',
            options={'managed': False},
        ),
    ]
