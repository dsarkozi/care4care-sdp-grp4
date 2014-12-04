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
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=75)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('comment', models.CharField(max_length=200, blank=True)),
                ('date', models.DateField(null=True)),
                ('start_time', models.IntegerField(null=True, blank=True)),
                ('frequency', models.SmallIntegerField(choices=[(0, 'Once'), (1, 'Weekly'), (2, 'Monthly')])),
                ('recursive_day', models.CharField(max_length=150, blank=True)),
                ('km', models.SmallIntegerField(blank=True, default=0)),
                ('duration', models.SmallIntegerField()),
                ('category', models.SmallIntegerField(choices=[(1, 'Shopping'), (2, 'Visit'), (3, 'Transport'), (4, 'Other')])),
                ('other_category', models.CharField(max_length=100, blank=True)),
                ('type', models.BooleanField(default=None)),
                ('place', models.TextField(blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('visibility', models.SmallIntegerField(default=2)),
                ('branch', models.ForeignKey(to='C4CApplication.Branch')),
                ('regular_job', models.ForeignKey(null=True, to='C4CApplication.Job', on_delete=django.db.models.deletion.SET_NULL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mail', models.EmailField(max_length=75, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('picture', models.ImageField(upload_to='images/images_profile/', storage=C4CApplication.models.member.OverwriteStorage(), blank=True, null=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('tag', models.SmallIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('mobile', models.CharField(max_length=15, blank=True)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('register_date', models.DateField(default='2014-12-04')),
                ('street', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=4)),
                ('town', models.CharField(max_length=100)),
                ('visibility', models.SmallIntegerField(default=2)),
                ('time_credit', models.BigIntegerField(default=0)),
                ('branch', models.ManyToManyField(to='C4CApplication.Branch')),
                ('job', models.ManyToManyField(null=True, blank=True, to='C4CApplication.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('member_source', models.ForeignKey(related_name='source', to='C4CApplication.Member')),
                ('member_target', models.ForeignKey(related_name='target', to='C4CApplication.Member')),
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
            field=models.ManyToManyField(null=True, blank=True, to='C4CApplication.Member', through='C4CApplication.Relationship'),
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
