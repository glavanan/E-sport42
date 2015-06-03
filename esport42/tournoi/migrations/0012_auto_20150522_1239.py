# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0011_tournament_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='bg_image',
            field=models.ImageField(default=b'/static/img/site/logo_esport42.jpg', upload_to=b'static/post/img'),
            preserve_default=True,
        ),
    ]
