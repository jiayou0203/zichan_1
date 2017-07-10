# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_delete_xinxisouji'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bloguser',
            table='data_blog_user',
        ),
    ]
