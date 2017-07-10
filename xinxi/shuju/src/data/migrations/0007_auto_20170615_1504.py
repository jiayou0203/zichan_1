# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20170615_1441'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
        migrations.DeleteModel(
            name='xinxisouji',
        ),
    ]
