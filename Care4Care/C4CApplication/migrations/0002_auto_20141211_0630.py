# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('C4CApplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='eid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='register_date',
            field=models.DateField(default='2014-12-11'),
            preserve_default=True,
        ),
    ]
