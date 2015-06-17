# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tmp_name', models.CharField(default=b'Tree', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=5)),
                ('txn_id', models.CharField(max_length=256, blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(related_name='team_admin', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('tag', models.CharField(unique=True, max_length=5)),
                ('nbteams', models.IntegerField()),
                ('player_per_team', models.IntegerField()),
                ('max_player', models.IntegerField()),
                ('template', models.IntegerField()),
                ('price', models.IntegerField()),
                ('game_name', models.CharField(max_length=40)),
                ('receiver_email', models.CharField(max_length=256, blank=True)),
                ('place', models.CharField(max_length=256)),
                ('rules', models.FileField(upload_to=b'static/tournament/rules', blank=True)),
                ('admin', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=b'static/post/img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(to='tournoi.Tournament')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teams',
            name='tournament',
            field=models.ForeignKey(to='tournoi.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phase',
            name='tournament',
            field=models.ForeignKey(to='tournoi.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apost',
            name='tournament',
            field=models.ForeignKey(to='tournoi.Tournament'),
            preserve_default=True,
        ),
    ]
