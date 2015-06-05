# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournoi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='admin',
            field=models.ForeignKey(related_name='team_admin', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teams',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 16, 51, 45, 195617, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teams',
            name='tag',
            field=models.CharField(default='FCK', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teams',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 16, 52, 8, 874456, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
