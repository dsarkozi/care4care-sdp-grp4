# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('town', models.CharField(max_length=200)),
                ('branch_officer', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=200)),
                ('donation', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=200)),
                ('start_time', models.IntegerField(default=0)),
                ('frequency', models.SmallIntegerField(default=0, choices=[(0, 'once'), (1, 'daily'), (2, 'weekly'), (3, 'monthly'), (4, 'yearly')])),
                ('km', models.SmallIntegerField(default=0)),
                ('time', models.SmallIntegerField(default=0)),
                ('category', models.SmallIntegerField(choices=[(1, 'shopping'), (2, 'visit'), (3, 'transport')])),
                ('type', models.BooleanField(default=None)),
                ('address', models.CharField(max_length=200)),
                ('accepted', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('visibility', models.SmallIntegerField(default=1)),
                ('branch', models.ForeignKey(to='C4CApplication.Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mail', models.EmailField(primary_key=True, serialize=False, max_length=75)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField(default='2014-01-01')),
                ('tag', models.SmallIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('mobile', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=15)),
                ('register_date', models.DateField(default='2014-11-14')),
                ('dash_board_text', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('visibility', models.SmallIntegerField(default=2)),
                ('time_credit', models.BigIntegerField(default=0)),
                ('branch', models.ManyToManyField(to='C4CApplication.Branch')),
                ('job', models.ManyToManyField(to='C4CApplication.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type', models.SmallIntegerField(default=0, choices=[(0, 'nothing'), (1, 'important'), (2, 'question'), (3, 'information')])),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(to='C4CApplication.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([('mail', 'number')]),
        ),
        migrations.AddField(
            model_name='member',
            name='message',
            field=models.ManyToManyField(to='C4CApplication.Message', through='C4CApplication.Mailbox'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='relation',
            field=models.ManyToManyField(to='C4CApplication.Member', through='C4CApplication.Relationship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailbox',
            name='member',
            field=models.ForeignKey(to='C4CApplication.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailbox',
            name='message',
            field=models.ForeignKey(to='C4CApplication.Message'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([('mail', 'number')]),
        ),
    ]
