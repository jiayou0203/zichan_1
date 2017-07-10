# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_xinxisouji'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xinxisouji',
            old_name='body',
            new_name='pcbody',
        ),
        migrations.RenameField(
            model_name='xinxisouji',
            old_name='tiemstamp',
            new_name='pctiemstamp',
        ),
    ]
