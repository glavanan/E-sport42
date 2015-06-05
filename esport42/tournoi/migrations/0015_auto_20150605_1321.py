# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0014_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tag',
            field=models.CharField(default='tag', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teams',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teams',
            name='tag',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
