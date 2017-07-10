# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='xinxisouji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pcaddress', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('tiemstamp', models.DateTimeField()),
                ('pcname', models.CharField(max_length=30)),
            ],
        ),
    ]
