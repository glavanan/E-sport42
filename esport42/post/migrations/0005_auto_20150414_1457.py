# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.TextField(default='Lol ceci est un resume'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=b'static/post/img/'),
            preserve_default=True,
        ),
    ]
