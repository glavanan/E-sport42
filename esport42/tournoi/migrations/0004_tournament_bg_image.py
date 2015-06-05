# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0003_auto_20150522_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='bg_image',
            field=models.ImageField(default='tmp', upload_to=b'static/post/img'),
            preserve_default=False,
        ),
    ]
