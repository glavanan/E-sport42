# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournoi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='end_reg',
            field=models.DateField(default='2015-06-27'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='end_tou',
            field=models.DateField(default='2015-06-29'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='pool',
            field=models.ManyToManyField(related_name='pool', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_reg',
            field=models.DateField(default='2015-06-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_tou',
            field=models.DateField(default='2015-06-27'),
            preserve_default=False,
        ),
    ]
