# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=30)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('first_name', models.CharField(max_length=40, blank=True)),
                ('last_name', models.CharField(max_length=40, blank=True)),
                ('address', models.TextField(blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('nationality', models.CharField(default=b'FR', max_length=40, blank=True)),
                ('phone', models.CharField(max_length=14, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
