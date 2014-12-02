# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import C4CApplication.models.member
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('town', models.CharField(max_length=200)),
                ('branch_officer', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=200)),
                ('donation', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('comment', models.CharField(max_length=200)),
                ('date', models.DateField(default='2014-12-02')),
                ('start_time', models.IntegerField(default=0)),
                ('frequency', models.SmallIntegerField(choices=[(0, 'Once'), (2, 'Weekly'), (3, 'Monthly')], default=0)),
                ('recursive_day', models.CharField(blank=True, max_length=150)),
                ('km', models.SmallIntegerField(default=0)),
                ('time', models.SmallIntegerField(default=0)),
                ('category', models.SmallIntegerField(choices=[(1, 'Shopping'), (2, 'Visit'), (3, 'Transport'), (4, 'Other')])),
                ('other_category', models.CharField(max_length=100)),
                ('type', models.BooleanField(default=None)),
                ('address', models.CharField(max_length=200)),
                ('accepted', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('visibility', models.SmallIntegerField(default=1)),
                ('branch', models.ForeignKey(null=True, to='C4CApplication.Branch', blank=True)),
                ('occurence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='C4CApplication.Job', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='images/images_profile/', storage=C4CApplication.models.member.OverwriteStorage())),
                ('birthday', models.DateField(default='2014-01-01')),
                ('tag', models.SmallIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('mobile', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=15)),
                ('register_date', models.DateField(default='2014-12-02')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
            field=models.ManyToManyField(to='C4CApplication.Member', through='C4CApplication.Relationship'),
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
