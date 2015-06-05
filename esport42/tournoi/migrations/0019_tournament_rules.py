# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0018_tournament_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='rules',
            field=models.FileField(upload_to=b'static/post/img', blank=True),
            preserve_default=True,
        ),
    ]
