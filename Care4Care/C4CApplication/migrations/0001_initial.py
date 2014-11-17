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
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=200)),
                ('start_time', models.IntegerField()),
                ('frequency', models.SmallIntegerField(choices=[(0, 'once'), (1, 'daily'), (2, 'weekly'), (3, 'monthly'), (4, 'yearly')])),
                ('km', models.SmallIntegerField(default=0)),
                ('time', models.SmallIntegerField()),
                ('category', models.SmallIntegerField(choices=[(1, 'shopping'), (2, 'visit'), (3, 'transport')])),
                ('type', models.BooleanField(default=None)),
                ('address', models.CharField(max_length=200)),
                ('accepted', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(to='C4CApplication.Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mail', models.EmailField(max_length=75, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('tag', models.SmallIntegerField(choices=[(0, 'non_member'), (1, 'member'), (2, 'verified'), (3, 'volunteer'), (4, 'branch_officer'), (5, 'bp_admin')])),
                ('status', models.BooleanField(default=True)),
                ('mobile', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=15)),
                ('register_date', models.DateField()),
                ('dash_board_text', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('visibility', models.SmallIntegerField(choices=[(1, 'anyone'), (2, 'verified'), (4, 'favorites'), (8, 'network')], default=2)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type', models.SmallIntegerField(choices=[(0, 'nothing'), (1, 'important'), (2, 'question'), (3, 'information')], default=0)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
