# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20150413_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='/static/img/Drinking_lcs.jpg', max_length=1024),
            preserve_default=False,
        ),
    ]
