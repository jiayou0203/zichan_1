# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_blogus'),
    ]

    operations = [
        migrations.CreateModel(
            name='xinxisouji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pcaddress', models.CharField(max_length=30)),
                ('pcbody', models.TextField()),
                ('pctiemstamp', models.DateTimeField()),
                ('pcname', models.CharField(max_length=30)),
            ],
        ),
    ]
