# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='bg_image',
            field=models.ImageField(default='tmpok', upload_to=b'static/post/img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='max_player',
            field=models.IntegerField(default=13),
            preserve_default=False,
        ),
    ]
