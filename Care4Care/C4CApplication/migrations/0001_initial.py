# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion

import C4CApplication.models.member


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('branch_town', models.CharField(max_length=200)),
                ('branch_officer', models.EmailField(max_length=75)),
                ('street', models.CharField(max_length=200, blank=True)),
                ('zip', models.CharField(max_length=4, blank=True)),
                ('town', models.CharField(max_length=100, blank=True)),
                ('donation', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('comment', models.CharField(default='', max_length=200, blank=True)),
                ('date', models.DateField(null=True)),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('frequency', models.SmallIntegerField(choices=[(0, 'Once'), (1, 'Weekly'), (2, 'Monthly')])),
                ('recursive_day', models.CharField(max_length=150, blank=True)),
                ('km', models.SmallIntegerField(default=0, blank=True)),
                ('duration', models.SmallIntegerField()),
                ('category', models.SmallIntegerField(choices=[(1, 'Shopping'), (2, 'Visit'), (3, 'Transport'), (4, 'Other')])),
                ('other_category', models.CharField(max_length=100, blank=True)),
                ('type', models.BooleanField(default=True)),
                ('place', models.TextField(blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('visibility', models.SmallIntegerField(default=2)),
                ('branch', models.ForeignKey(to='C4CApplication.Branch')),
                ('regular_job', models.ForeignKey(to='C4CApplication.Job', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mail', models.EmailField(primary_key=True, max_length=75, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('picture', models.ImageField(storage=C4CApplication.models.member.OverwriteStorage(), upload_to='images/images_profile/', blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('tag', models.SmallIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('mobile', models.CharField(max_length=15, blank=True)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('register_date', models.DateField(default='2014-12-05')),
                ('street', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=4)),
                ('town', models.CharField(max_length=100)),
                ('visibility', models.SmallIntegerField(default=2)),
                ('time_credit', models.BigIntegerField(default=0)),
                ('branch', models.ManyToManyField(to='C4CApplication.Branch')),
                ('job', models.ManyToManyField(to='C4CApplication.Job', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type', models.SmallIntegerField(choices=[(0, 'nothing'), (1, 'important'), (2, 'question'), (3, 'information')], default=0)),
                ('date', models.DateField()),
                ('member_sender', models.ForeignKey(to='C4CApplication.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('member_source', models.ForeignKey(to='C4CApplication.Member', related_name='source')),
                ('member_target', models.ForeignKey(to='C4CApplication.Member', related_name='target')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([('member_sender', 'number')]),
        ),
        migrations.AddField(
            model_name='member',
            name='relation',
            field=models.ManyToManyField(to='C4CApplication.Member', through='C4CApplication.Relationship', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailbox',
            name='member_receiver',
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
