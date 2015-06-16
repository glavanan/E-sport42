# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_auto_20150614_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='looser_braket',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
