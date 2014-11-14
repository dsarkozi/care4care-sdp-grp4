# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('C4CApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='donation',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
