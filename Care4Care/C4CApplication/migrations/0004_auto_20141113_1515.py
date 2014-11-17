# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('C4CApplication', '0003_branch_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='visibility',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='tag',
            field=models.SmallIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='visibility',
            field=models.SmallIntegerField(default=2),
            preserve_default=True,
        ),
    ]
